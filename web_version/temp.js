
function timer(ms) {
        return new Promise(res => setTimeout(res, ms));
    }

    async function load() { // We need to wrap the loop into an async function for this to work
        for (var i = 0; i < 3; i++) {
            console.log(i);
            await timer(300); // then the created Promise can be awaited
            console.log('hhahahaha');
            await timer(2000);
            console.log('20000000000000000000')
        }
    }
    load();

