/**
 * Created by mengy on 2017/3/14.
 */
console.log(qs);
console.log(account_id);

$(document).ready(function() {
    function getdata() {
        var xdata= [], ydata= [];
        $.ajax(
            {
                url: '/dash/get_linked_account_billing',
                data: {qs: qs, account_id: account_id},
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


    var myChart = echarts.init(document.getElementById('echart-account-async'));
    myChart.showLoading();
    var res = getdata();
    console.log(res[0]);
    console.log(res[1]);

    var option = {
        title: {
            text: 'linked account: ' + account_id,
            top: 'top',
            left: 'left'
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
        series: [{
            name: '消费',
            type: 'bar',
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
        }]
    };
    myChart.hideLoading();
    myChart.setOption(option);

});