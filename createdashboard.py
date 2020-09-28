from datadog import initialize, api

options = {
    'api_key': '<your Datadog API Key>',
    'app_key': '<your Datadog App Key>'
}

initialize(**options)

title = 'The Nathan Random Number and MongoDB Network Usage Dashboard'
widgets = [
      {
         'definition':{
            'type':'timeseries',
            'requests':[
               {
                  'q':'avg:custom.randomnumber{device:nates-macbook-pro}',
                  'display_type':'line',
                  'style':{
                     'palette':'orange',
                     'line_type':'solid',
                     'line_width':'thick'
                  },
                  'on_right_yaxis':False
               }
            ],
            'yaxis':{
               'label':'',
               'scale':'linear',
               'min':'auto',
               'max':'auto',
               'include_zero':True
            },
            'title':'custom.randomnumber',
            'time':{
               
            },
            'show_legend':False,
            'legend_size':'0'
         }
      },
      {
         'definition':{
            'type':'timeseries',
            'requests':[
               {
                  'q':'anomalies(avg:mongodb.network.bytesinps{*}, \'basic\', 4)',
                  'display_type':'line',
                  'style':{
                     'palette':'dog_classic',
                     'line_type':'solid',
                     'line_width':'normal'
                  }
               }
            ],
            'yaxis':{
               'label':'',
               'scale':'linear',
               'min':'auto',
               'max':'auto',
               'include_zero':True
            },
            'title':'MongoDB Network Usage',
            'time':{
               
            },
            'show_legend':False
         }
      }
]
layout_type = 'ordered'
description = 'A dashboard with random numbers and information about MongoDB memory usage.'
is_read_only = True
notify_list = ['ncontino@u.rochester.edu']
template_variables = []

saved_views = []

print(api.Dashboard.create(title=title,
                     widgets=widgets,
                     layout_type=layout_type,
                     description=description,
                     is_read_only=is_read_only,
                     notify_list=notify_list,
                     template_variables=template_variables,
                     template_variable_presets=saved_views))

