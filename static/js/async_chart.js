/**
 * Created by mengy on 2017/2/23.
 */

console.log(qs);

$(document).ready(function() {
    function getdata() {
        var xdata= [], ydata= [];
        $.ajax(
            {
                url: '/test_0',
                data: {qs: qs},
                async: false,
                success: function(data) {
                    console.log(data);
                    if(data){
                        for(var key in data){
                            xdata.push(key);
                            ydata.push( parseInt(data[key]) );
                        }
                    }
                }
            }
        );
        return [xdata,ydata];
    }


    var myChart = echarts.init(document.getElementById('echart-test-async'));
myChart.showLoading();
var res = getdata();
console.log(res[0]);
console.log(res[1]);

var option = {
    title: {
        text: 'ECharts test async'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'line'
        }
    },
    legend: {
        data:['消费']
    },
    xAxis: {
        name: 'AWS资源名',
        type: 'category',
        axisLabel: {
            interval: 0,
            rotate: 13
        },
        data: res[0]
    },
    yAxis: {
        name: '费用（元）',
        type: 'value',
        data: []
    },
    dataZoom: [
        {
            id: 'dataZoomX-inside',
            type: 'inside',
            xAxisIndex: [0],
            filterMode: 'filter',
            start: 0,
            end: 100
        },
        {
            id: 'dataZoomX-slider',
            type: 'slider',
            bottom: -20,
            xAxisIndex: [0],
            filterMode: 'filter',
            start: 0,
            end: 100
        }
    ],
    series: [
        {
            name: '消费',
            type: 'line',
            itemStyle: {
                normal: {
                    opacity: 0.8
                }
            },
            symbolSize: function (val) {
                return val[2] * 40;
            },
            //data: [["14.616","7.241","0.896"],["3.958","5.701","0.955"],["2.768","8.971","0.669"],["9.051","9.710","0.171"],["14.046","4.182","0.536"],["12.295","1.429","0.962"],["4.417","8.167","0.113"],["0.492","4.771","0.785"],["7.632","2.605","0.645"],["14.242","5.042","0.368"]]
            data: res[1]
        }
    ]
};
myChart.hideLoading();
myChart.setOption(option);

});


/*
var myChart_async = echarts.init(document.getElementById('echart-test-async'));
// 显示标题，图例和空的坐标轴
myChart_async.setOption({
    title: {
        text: '异步数据加载示例'
    },
    tooltip: {},
    legend: {
        data:['销量']
    },
    xAxis: {
        data: []
    },
    yAxis: {},
    series: [{
        name: '销量',
        type: 'bar',
        data: []
    }]
});

// 异步加载数据
$.get({
    url: '/test_0',
    data: {qs: qs}
}).done(function (data) {
    // 填入数据
    console.log(data);
    myChart_async.setOption({
        xAxis: {
            data: data.categories
        },
        series: [{
            // 根据名字对应到相应的系列
            name: '销量',
            data: data.data
        }]
    });
});
*/

/*
var myChart_async = echarts.init(document.getElementById('echart-test-async'));

$.get().done(function () {
    myChart_async.setOption({
        title: {
            text: 'Echarts-test-async'
        },
        tooltip: {},
        legend: {
            data:['费用']
        },
        xAxis: {
            data: ["EC2", "S3", "RDS", "xx", "yy", "zz"]
        },
        yAxis: {},
        series: [{
            name: '费用',
            type: 'bar',
            data: [5, 5, 5, 5, 5, 5]
        }]
    });
});
*/