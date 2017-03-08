/**
 * Created by mengy on 2017/2/23.
 */
var myChart = echarts.init(document.getElementById('echart-test-static'));
var option = {
    title: {
        text: 'test static',
        subtext: 'Search group by: '
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            style: 'line'
        }
    },
    legend: {
        data:['费用','tag1','tag2']
    },
    xAxis: {
        name: 'AWS资源/服务名',
        type: 'category',
        data: ["AmazonEC2", "AmazonS3", "AmazonCloudWatch", "AmazonSNS", "AmazonDynamoDB", "AWSDataTransfer"]
    },
    yAxis: {
        name: '费用（元）'
    },
    series: [
        {
            name: '费用',
            type: 'bar',
            data: [20, 20, 36, 10, 10, 20]
        },
        {
            name: 'tag1',
            type: 'bar',
            data: [10, 20, 15, 20, 12, 20]
        },
        {
            name: 'tag2',
            type: 'bar',
            data: [1, 2, 3, 4, 5, 6]
        }
    ]
};
myChart.setOption(option);