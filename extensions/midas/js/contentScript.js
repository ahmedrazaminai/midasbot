import $ from 'jquery';

function ws() {
    console.log('ws')
    const websk = new WebSocket('ws://localhost:8080');
    
    websk.onopen = function () {
        websk.send('Hello Server!');
        websk.onmessage = function (event) {
            console.log(event.data);
        }
    };
}

const t = 30000

function waitForSelector(selector, timeout = t){
    let counter = 0
    interval = setInterval(() => {
        counter++
        if (counter >= timeout) {
            clearInterval(interval)
            throw new Error(`Timeout waiting for selector ${selector}`)
        }
        if ($(selector)) {
            clearInterval(interval)
            return $(selector)
        }
    }, 1)
}

function waitForTimeout(timeout){
    setTimeout(() => {}, timeout)
}

function select(selector, timeout=t){
    return waitForSelector(selector, timeout)
}

function page_click(selector, timeout = t) {
    select(selector, timeout).click()
    return true
}


function insert(selector, string, timeout = t){
    select(selector, timeout).val(string);
    return true
}


function page1() {
    page_click('.UserTabBox_switch_btn__428iM')
}
   

function run(url) {
    document.location.href = 'https://www.midasbuy.com/midasbuy/tr/buy/pubgm';
    page_click('[data-iformat="login_control"]');
    page_click('[data-iformat="login"]');
    insert('.input.email-input input', 'username');
    insert('[type="password"]', 'password');
    page_click('.sign-in-btn');
}

// ws()