/**
 * @param {string[]} keyName
 * @param {string[]} keyTime
 * @return {string[]}
 */
 /*
1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
 Key-card systems @ offices
 Save : name and time of usage -> emit alert if someone uses their card >= 3 times in an hour period
 Access times in HH:MM format : time = (hours * 60) + minutes
 List of unique worker names : whoever got an alert -> alpha sort later

SingleDayusage versus other granularity usages 

 Building alerting system : bad in office
 Generate an alert on a metric threshold surpassed in a given time window :-) like AWS Cloudwatch metrics
 */
var alertNames = function(keyName, keyTime) {
    let workersWithAlerts = new Set()
    // for each callback index param
    let workerAlerts = new Map()
    let hourDiff = 60 // constand standard
    // Single day : stream unsored -> need to consider this too gaaah!
    keyName.forEach((name,index) => {
        // In prod code, we'd exec a std time conversion :-)
        let curTime = stdTimeConvert(keyTime[index])
        if(!workerAlerts.has(name)){
            workerAlerts.set(name,[])
        }
        // https://dcodesnippet.com/copy-javascript-array/
        let curAlerts = workerAlerts.get(name)
        curAlerts.push(curTime)
    })
    workerAlerts.forEach((alerts,worker) => {
        alerts.sort((a,b) => { return Number(a) - Number(b)})
        if(alerts.length >= 3){
            for(let i = 0; i < alerts.length - 2; i++){
    //         // .at() : bwsr support neg idx compatible
                let aOne = alerts.at(i)
                let aTwo = alerts.at(i+2)
                if(aTwo - aOne <= 60){
                    workersWithAlerts.add(worker)
                }
            }
        }
    })
    // return [...workersWithAlerts].sort((a,b) => { return a.localeCompare(b) })
    return Array.from(workersWithAlerts).sort((a,b) => { return a.localeCompare(b) })
};

// Convert : human-readable time => computer time
function stdTimeConvert(humanTime){
    let timeEls = humanTime.split(":")
    let stdTime = 60*Number(timeEls[0]) + Number(timeEls[1])
    return stdTime
}
