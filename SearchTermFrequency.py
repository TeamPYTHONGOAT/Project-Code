def Get SearchFrequency(search_term):
	"""
	This function takes a search term as its input and returns a list of normalized scores per month since 1/1/2004.
	Normalized score means that the month which saw the most searches becomes 100, and everything else gets scaled appropriately.
	"""

	search = search_term
	url = ('https://www.google.com/trends/fetchComponent?hl=en-US&q={}&cid=TIMESERIES_GRAPH_0&export=5&w=500&h=300'
       .format(search))

	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

	headers={'User-Agent':user_agent,}
	request=urllib.request.Request(url,None,headers)
	response = urllib.request.urlopen(request)
	data = response.read()

	soup = BeautifulSoup(data,"lxml")

	graph_date = str(soup.findAll("script", {"type":"text/javascript"})[3])

	from pprint import pprint
	json_frmt = graph_date[573:len(graph_date)-386]
	json_frmt

	def convert_mnth(month):
    frmt = month[0:3]+' 01 '+month[len(month)-4:len(month)]
    dt_frmt = datetime.date(datetime.strptime(convert_mnth('January 2004'), '%b %d %Y'))
    return dt_frmt

	split_data = json_frmt.split(',')

	data_points = []
	i=0

	for element in split_data:
	    if element.startswith('"f":'):
	        data_points.append([element, split_data[i+3]])
	    i+=1

	data_points = list(map(lambda x: [x[0][5:len(x[0])-2], int(x[1])], data_points))