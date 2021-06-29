# import cx_Oracle
import json
import re

from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
# Include the `fusioncharts.py` file that contains functions to embed the charts.

from .fusioncharts import FusionCharts


def myFirstChart(request):
    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Main Order Camp"
    # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Month"
    chartConfig["yAxisName"] = "Revenues (in USD)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    widgetDataSource = OrderedDict()
    widgetConfig = OrderedDict()
    widgetConfig["caption"] = "Nordstrom's Customer Satisfaction Score for 2017"
    widgetConfig["lowerLimit"] = "0"
    widgetConfig["upperLimit"] = "100"
    widgetConfig["showValue"] = "1"
    widgetConfig["numberSuffix"] = "%"
    widgetConfig["theme"] = "fusion"
    widgetConfig["showToolTip"] = "0"

    # The `colorData` dict contains key-value pairs of data for ColorRange of dial
    colorRangeData = OrderedDict()
    colorRangeData["color"] = [{
        "minValue": "0",
        "maxValue": "50",
        "code": "#F2726F"
    },
        {
            "minValue": "50",
            "maxValue": "75",
            "code": "#FFC533"
        },
        {
            "minValue": "75",
            "maxValue": "100",
            "code": "#62B58F"
        }
    ]
    # Load dial indicator values from simple string array# e.g.dialValues = ["52", "10", "81", "95"]

    dialValues = ["81"]
    # Convert the data in the `dialData` array into a format that can be consumed by FusionCharts.
    dialData = OrderedDict()
    dialData["dial"] = []

    widgetDataSource["chart"] = widgetConfig
    widgetDataSource["colorRange"] = colorRangeData
    widgetDataSource["dials"] = dialData

    dataSource["chart"] = chartConfig

    # f = open("data.json", "r")
    f = open("test.json", "r")
    c = re.sub(" *\n* }", "}", f.read())
    data = json.loads(c)
    json.dumps(data).replace("'", '"')
    dataSource["data"] = []
    for i in data["data"]:
        dataSource["data"].append(i)
    # dataSource = "data.json"
    f.close()
    for i in range(len(dialValues)):
        dialData["dial"].append({
        "value": dialValues[i]
    })
    var = "This is an output example" #use this as an example on how to write into the frontend
    column2D = FusionCharts("column2d", "myFirstChart", "100%", "400", "myFirstchart-container", "json", dataSource)
    angulargaugeWidget = FusionCharts("angulargauge", "myFirstWidget", "100%", "200", "myFirstwidget-container", "json", widgetDataSource)
    return render(request, 'index.html', {
        'output': column2D.render(),
        'output2': angulargaugeWidget.render(),
        'output3': var #this is how we're returning the value to the front end
    })