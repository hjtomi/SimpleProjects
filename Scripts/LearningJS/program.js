//console.log("apple".concat("hello dumbass"));

function addNumbers(a, b) {
    return a + b
}

//number = addNumbers(5, 5)
//if (number == 3) {
//    console.log('number is 3')
//}
//else if (number == 11) {
//    console.log('number is 11')
//}
//else {
//    console.log('number is '+number)
//}

var breakfast = ['coffee', 'pencakes', 'yoghurt']
breakfast.push('nyan')
//console.log(breakfast.reverse())

var jsObject = {
    key: 'value',
    anotherKey: 'anotherValue',
    5: 5,
    allValues: function() {
        console.log(Object.values(jsObject))
    }
}
//console.log(jsObject.key)
//console.log(jsObject['anotherKey'])
//console.log(jsObject[5])
//console.log(jsObject.cat)
//console.log(jsObject['cat'])

function myFunction() {
    document.getElementById('myId').innerHTML = 'This is not so random anymore.';
    const myClasses = Object.values(document.getElementsByClassName('myClassName'));
    console.log(myClasses.constructor)
    myClasses.forEach((value, index) => myClasses[index].innerHTML = 'the same value');
}
