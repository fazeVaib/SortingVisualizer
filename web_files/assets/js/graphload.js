window.onload = function () {

    var slider = document.getElementById("myRange");
    var speedSlider = document.getElementById("speedSlider");
    var speed = speedSlider.value;
    var sortButton = this.document.getElementById("sortButton");
    var sortRadio = document.getElementsByName('r');
    var audio = new Audio('./web_files/assets/js/s3.m4a');
    audio.muted = false;


    var RED = "#CD5A41";
    var GREEN = "#ACE797";
    var LIME = "#FAFAD9";
    var LIGHT_GREY = "#EAE8E8";
    var BLACK = "#1E1E1A";
    var DARK_GREEN = "#127F43";

    var mydata = [12, 19, 3, 5, 2, 3];
    var mylabel = [0, 1, 2, 3, 4, 5];
    var myColors = Array(6).fill("#EAE8E8");
    // console.log(myColors); 

    var ctx = document.getElementById('myChart').getContext('2d');
    
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: mylabel,
            datasets: [{
                label: "Value of bar: ",
                data: mydata,
                borderColor: "#FFFFFF",
                backgroundColor: myColors,
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

        myColors = Array.apply(null, { length: num }).fill("#EAE8E8");
        myChart.data.datasets[0].backgroundColor = myColors;
        myChart.data.datasets[0].data = mydata;
        myChart.update();
    }

    // Update the current slider value (each time you drag the slider handle)
    slider.oninput = function () {
        generateData(slider.value);
    };
    
    // Update the current SpeedSlider value (each time you drag the slider handle)
    speedSlider.oninput = function () {
        speed = speedSlider.value;
    };
    
    function timer(ms) {
        return new Promise(res => setTimeout(res, ms));
    }

    function swap(arr, first_Index, second_Index) {
        var temp = arr[first_Index];
        arr[first_Index] = arr[second_Index];
        arr[second_Index] = temp;
    }

    async function insertionSort(arr, speed) {
        var len = arr.length;
        for (var i = 0; i < len; i++) {
            var el = arr[i];
            myColors[i] = BLACK;
            myChart.data.datasets[0].backgroundColor = myColors;
            myChart.update();

            var j;

            for (j = i - 1; j >= 0 && arr[j] > el; j--) {
                myColors[j] = RED;
                arr[j + 1] = arr[j];
                myChart.data.datasets[0].backgroundColor = myColors;
                mydata = arr;
                myChart.data.datasets[0].data = mydata;
                myChart.update();
                await timer(speed);
                myColors[j] = DARK_GREEN;
                myChart.data.datasets[0].backgroundColor = myColors;
                myChart.update();

            }
            arr[j + 1] = el;
            myColors[i] = DARK_GREEN;
            myChart.data.datasets[0].backgroundColor = myColors;
            myChart.update();
            mydata = arr;
            myChart.data.datasets[0].data = mydata;
            myChart.update();
        }

        sortButton.disabled = false;
        slider.disabled = false;
        speedSlider.disabled = false;
    }

    async function bubble_Sort(arr, speed) {

        var len = arr.length,
            i, j, stop;

        for (i = 0; i < len; i++) {
            for (j = 0, stop = len - i; j < stop - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    myColors[j] = RED;
                    myColors[j + 1] = RED;
                    swap(arr, j, j + 1);
                    mydata = arr;
                    myChart.data.datasets[0].data = mydata;
                    myChart.data.datasets[0].backgroundColor = myColors;
                    myChart.update();
                    // audio.play();
                    await timer(speed);
                    myColors[j] = LIGHT_GREY;
                    myColors[j + 1] = LIGHT_GREY;
                    myChart.data.datasets[0].backgroundColor = myColors;
                    myChart.update();
                }
                else {

                    myColors[j] = GREEN;
                    myColors[j + 1] = GREEN;
                    myChart.data.datasets[0].backgroundColor = myColors;
                    myChart.update();
                    await timer(speed);
                    myColors[j] = LIGHT_GREY;
                    myColors[j + 1] = LIGHT_GREY;
                    myChart.data.datasets[0].backgroundColor = myColors;
                    myChart.update();

                }
            }
            myColors[len - i] = DARK_GREEN;
            myColors[len - i - 1] = DARK_GREEN;
            myChart.data.datasets[0].backgroundColor = myColors;
            myChart.update();
        }
        myColors[0] = DARK_GREEN;
        myChart.data.datasets[0].backgroundColor = myColors;
        myChart.update();

        sortButton.disabled = false;
        slider.disabled = false;
        speedSlider.disabled = false;
    }
    
    sortButton.onclick = function () {

        sortButton.disabled  = true;
        slider.disabled = true;
        speedSlider.disabled = true;

        if (sortRadio[0].checked) {
            console.log(sortRadio[0].value);
            bubble_Sort(mydata, 1001-speed);
        }
        else if (sortRadio[1].checked) {
            console.log(sortRadio[1].value);
            insertionSort(mydata, 1001-speed);

        }
        else if (sortRadio[2].checked) {
            console.log(sortRadio[2].value);
        }
        else if (sortRadio[3].checked) {
            console.log(sortRadio[3].value);
        }
        else if (sortRadio[4].checked) {
            console.log(sortRadio[4].value);
        }
        else {
            console.log(sortRadio[5].value);
        }
        
        
    };
};