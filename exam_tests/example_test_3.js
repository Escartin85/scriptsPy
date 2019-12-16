// Write a function that converts user entered date formatted as M/D/YYYY to a format required by an API
// (YYYYMMDD). The parameter "userDate" and the return value are string

// For example, it should convert user entered date "12/31/2014" to "20141231" suitable for the API

function formatDate(userDate){
    // format from M/D/YYYY to YYYYMMDD
    var year = userDate.slice(-4);
    var day = userDate.slice(3, 5);
    var month = userDate.slice(0, 2);
    var newDate = year + month + day;
    return newDate;
}
