import math
from pyXSteam.XSteam import XSteam

pipe_dia_data ={
0.5	:0.1375,
0.75:0.15,
1	:0.1625,
1.5	:0.175,
2	:0.2,
3	:0.235,
4	:0.275,
6	:0.355,
8	:0.425,
10	:0.505,
12	:0.5725,
14	:0.62,
16	:0.6825,
18	:0.7675,
20	:0.8175,
24	:0.985,
30	:1.19}

insulation_thickness_data = {
1	: [0.0924, 1.5083],
1.5	:[0.0373, 1.1778],
2.5	:[-0.0289, 0.8997],
3	:[-0.0406, 0.831],
4	:[-0.049, 0.7024],
5	:[-0.0544, 0.6315],
6	:[-0.0574, 0.5838]}

wind_correction_data= {
5:
	{1	:[0.0079, 1.0456],
	1.5	:[0.0065, 1.0277],
	2	:[0.0049, 1.0206],
	2.5	:[0.004, 1.0167],
	3	:[0.0032, 1.0128],
	4	:[0.0031, 1.0086],
	6	:[0.0017, 1.0055]},
10:

	{1	:[0.0103, 1.0564],
	1.5	:[0.0076, 1.0349],
	2	:[0.0063, 1.0245],
	2.5	:[0.0056, 1.0192],
	3	:[0.0049, 1.0138],
	4	:[0.0037, 1.0087],
	6	:[0.0027, 1.0058]},
15:
	{1  :[0.0117, 1.0648],
	1.5	:[0.0085, 1.0409],
	2	:[0.007, 1.0294],
	2.5	:[0.0062, 1.0232],
	3	:[0.0054, 1.017],
	4	:[0.0043, 1.0113],
	6	:[0.0034, 1.006]}

}

trace_data ={
 '(1) 3/8 - OD' :	0.3,
 '(1) 1/2 - OD' :0.375,
 '(1) 5/8 - OD' : 0.5,
 '(1) 3/4 - OD' :	0.6,
 '(1) 3/4 - OD' :	0.6625,
 '(2) 1/2 - OD' :	0.7875,
 '(1) 3/4 - NPS' : 0.8625,
 '(2) 5/8 - OD' :	0.95,
 '(1) 1 - NPS' :	1.0625,
 '(2) 3/4 - OD' :	1.175,
 '(2) 1/2 - NPS' : 1.3375,
 '(2) 3/4 - NPS' : 1.65,
 '(3) 1/2 - NPS' : 1.95,
 '(2) 1 - NPS' : 2.05,
 '(3) 3/4 - NPS' : 2.5,
 '(3) 1 - NPS' : 3.1}

def calc_sat_temp(steam_pressure): # steam pressure in psig
	steamTable = XSteam(XSteam.UNIT_SYSTEM_FLS)
	return round(steamTable.tsat_p (float(steam_pressure) + 14.696),2) # psia to psig

def get_tracer_length(p, tracer):
	if p<=50:
		if tracer== '(1) 3/8 - OD' : return 60
		elif tracer in ['(1) 1/2 - OD', '(2) 1/2 - OD', '(2) 1/2 - NPS','(3) 1/2 - NPS']: return 120
		else: return 150

	elif p>50 or p<=70:
		if tracer== '(1) 3/8 - OD' : return 100
		elif tracer in ['(1) 1/2 - OD', '(2) 1/2 - OD', '(2) 1/2 - NPS','(3) 1/2 - NPS']: return 150
		else: return 200

	else:
		if tracer== '(1) 3/8 - OD' : return 100
		elif tracer in ['(1) 1/2 - OD', '(2) 1/2 - OD', '(2) 1/2 - NPS','(3) 1/2 - NPS']: return 150
		else: return 200




def dia_correction(NPS):
	return pipe_dia_data[NPS]

def thickness_correction(NPS, INS):
	if INS==2: return 1
	x1, x2 = insulation_thickness_data[INS][0], insulation_thickness_data[INS][1]
	return x1*math.log(NPS) + x2

def type_correction(k):
	return k*3.3313

def wind_correction(NPS, INS, wind_velocity):
	if wind_velocity==0: return 1
	x1, x2 = wind_correction_data[wind_velocity][INS][0], wind_correction_data[wind_velocity][INS][1]
	return x1*math.log(NPS) + x2

def get_k (insulation_type, T):
	if insulation_type=='fiber_glass': return (0.0006*T)+0.1833
	if insulation_type=='cal_si': return (0.0006*T)+0.211

def get_tracing(T2, Q2):
	for key, value in trace_data.items():
		temp = T2* value
		if temp> Q2: return key





def get_trace_calc(maintain_temp, steam_temp, amb_temp, pipe_dia, insulation_type, insulation_thickness, wind_velocity):
	avg_temp = (maintain_temp + steam_temp)/2
	T1 = avg_temp - amb_temp	
	Q1 = T1* dia_correction(pipe_dia)
	F1 = thickness_correction (pipe_dia, insulation_thickness)

	iavg_temp = (avg_temp + amb_temp)/2
	k = get_k(insulation_type, iavg_temp)
	F2 = type_correction(k)

	F3 = wind_correction(pipe_dia, insulation_thickness, wind_velocity)
	
	Q2= Q1*F1*F2*F3
	T2 = steam_temp- maintain_temp

	return Q2, get_tracing(T2, Q2)


def get_trace_result (input_data):
	base_data = {}
	pipe_data = {}

	for i in input_data[0]:
		base_data [i['name']] = i['value']
	
	steam_pressure= float(base_data['steam_pressure'])
	TT = float (base_data ['steam_temp'])
	Tamb = float(base_data['amb_temp'])
	wv = float(base_data['wind_velocity'])

	for i in input_data[1]:	
		if i['class'] in pipe_data:
			pipe_data[i['class']][next(iter(i))] = i[next(iter(i))]
		else:
			pipe_data[i['class']] = {next(iter(i)) : i[next(iter(i))]}
	
	for i, j in pipe_data.items():
		TP = float(j['maintain_temp'])
		NPS = float(j['pipe_dia'])
		INS = float(j['insulation_thickness'])
		ins_type = j['insulation_type']
		pipe_length= float(j['pipe_length'])

		trace = get_trace_calc(TP, TT, Tamb, NPS, ins_type, INS, wv)[1]
		heat_loss = get_trace_calc(TP, TT, Tamb, NPS, ins_type, INS, wv)[0]
		pipe_data[i]['trace'] = trace
		pipe_data[i]['heat_loss'] = round(heat_loss,3)

		steamTable = XSteam(XSteam.UNIT_SYSTEM_FLS)
		h = steamTable.hV_p(steam_pressure + 14.696) -steamTable.hL_p (steam_pressure + 14.696)

		#check


		pipe_data[i]['steam_require'] = round ((pipe_length* heat_loss/h),3)

		tracer_length = get_tracer_length(steam_pressure, trace)
		pipe_data[i]['tracer_length'] = tracer_length


	return pipe_data


test_d = [[{"name":"steam_pressure","value":""},{"name":"steam_temp","value":"366"},{"name":"amb_temp","value":"10"},\
{"name":"wind_velocity","value":"10"}],[{"line_id":"","class":"pipe_1"},{"description":"","class":"pipe_1"},\
{"pipe_length":"100","class":"pipe_1"},{"pipe_dia":"0.5","class":"pipe_1"},{"insulation_type":"fiber_glass","class":"pipe_1"},\
{"insulation_thickness":"2","class":"pipe_1"},{"maintain_temp":"100","class":"pipe_1"},{"":"Remove","class":"pipe_1"},\
{"line_id":"","class":"pipe_2"},{"description":"","class":"pipe_2"},{"pipe_length":"150","class":"pipe_2"},\
{"pipe_dia":"6","class":"pipe_2"},{"insulation_type":"cal_si","class":"pipe_2"},{"insulation_thickness":"1","class":"pipe_2"},\
{"maintain_temp":"150","class":"pipe_2"},{"":"Remove","class":"pipe_2"}]]

#print((get_trace_result(test_d)))




