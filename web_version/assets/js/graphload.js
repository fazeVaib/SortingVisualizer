window.onload = function () {

    var slider = document.getElementById("myRange");
    var output = document.getElementById("demoPrint");
    var sortButton = this.document.getElementById("sortButton");
    output.innerHTML = slider.value; // Display the default slider value

    var mydata = [12, 19, 3, 5, 2, 3];
    var mylabel = [0, 1, 2, 3, 4, 5];


    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: mylabel,
            datasets: [{
                label: '# of Votes',
                data: mydata,
                borderWidth: 1
            }]
        },
        options: {
            animation: {
                duration: 100
            },
            legend: false,
            scales: {
                yAxes: [{
                    display: false,
                    ticks: {
                        beginAtZero: true
                    }
                }],
                xAxes: [{
                    display: false,
                    categoryPercentage: 1.0,
                    barPercentage: 1.0
                }]
            }
        }
    });


    function generateData(num) {
        mydata = Array.apply(null, {
            length: num
        }).map(function () {
            return Math.floor(Math.random() * 100 % 100) + 1;
        });
        var temp = Array.apply(null, {
            length: num
        }).map(Number.call, Number);
        myChart.data.labels = temp;

        myChart.data.datasets[0].data = mydata;
        myChart.update();
    }

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        output.innerHTML = slider.value;
        generateData(slider.value);
    };

    function timer(ms) {
        return new Promise(res => setTimeout(res, ms));
    }

    async function Sort() { // We need to wrap the loop into an async function for this to work
        for (var i = 0; i < 10; i++) {
            mydata = Array.apply(null, {
                length: slider.value
            }).map(function () {
                return Math.floor(Math.random() * 100 % 100) + 1;
            });

            myChart.data.datasets[0].data = mydata;
            myChart.update();
            
            await timer(1000);
        }
    }

    sortButton.onclick = function () {
        Sort();
    };
};