function ws() {
    const client = new WebSocket('ws://localhost:8000/');
    client.onopen = () => {
        console.log('WebSocket Client Connected');
    }
    
    client.onmessage = (message) => {
        console.log(message.data)
        client.send('Hi there!');
    }
   
}

const t = 30000

function waitForSelector(selector, timeout = t){
    // let counter = 0
    for (let i = 0; i <= timeout; i++) {
        if (document.querySelector(selector)) {
            console.log(`Found selector ${selector}`)
            return document.querySelector(selector)
        }
        waitForTimeout(1)
    }
    console.log(`Timeout waiting for selector ${selector} after ${timeout}ms`)
    throw new Error(`Timeout waiting for selector ${selector}`)
}

function waitForTimeout(timeout){
    const sleep = (milliseconds) => {
        return new Promise(resolve => setTimeout(resolve, milliseconds))
    } 
    sleep(timeout).then(() => {})
}

function select(selector, timeout=t){
    return waitForSelector(selector, timeout)
}

function page_click(selector, timeout = t) {
    select(selector, timeout).click()
    return true
}


function insert(selector, string, timeout = t){
    select(selector, timeout).value = string;
    return true
}

function loginVerify(selector, page) {
    try {waitForSelector(selector, timeout=2000)} 
        catch (error) {login(page)};
}


function login(page) {
    const username = "moreiraccheyennegopaliwint@gmail.com"
    const password = "qweqwe123"

    const iconClick = () => page == 1 ? page_click('[cr="login"]') : page_click('[data-iformat="login_control"]')
    iconClick()
    insert('.input.email-input input', username, timeout=120000);
    insert('[type="password"]', password);
    // page_click('[type="password"]');
    // KeyboardEvent.apply(document.querySelector('[type="password"]'), {
        //     keyCode: 13,
    //     which: 13,
    //     key: "Enter",
    //     code: "Enter",
    //     charCode: 13,
    //     bubbles: true,
    //     cancelable: true,
    //     composed: true,
    // });
    // page_click('.sign-in-btn');
    waitForTimeout(2000)
    iconClick()
}


function page1() {
    page_click('.user-email')
    loginVerify('#headerVipcenterButton', 1)
    
}


function run() {
    window.addEventListener("load", function() {
        console.log('loaded')
        page1()
    }, false);
    // try{page_click('[data-iformat="login_control"]')}
    //     catch{page_click('.user-email')};
    // console.log('run2')
}

run()