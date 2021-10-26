const weekChange = (num) => {
    if (num > 0) {
        return ( <span className="green">
                    {"+" + num.toLocaleString()}
                </span> )
    }
    else if (num < 0) {
        return ( <span className="red">
                    {num.toLocaleString()}
                </span> )
    }
    else return <span>{num}</span>
}
const reportDate = (date) => {
    const calandarMonth = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    const x = date.split("-");
    let month = calandarMonth[parseInt(x[1]) - 1]
    let day = x[2]
    let year = x[0]
    return month +' '+ day +', '+ year;
}

export const format = {
    weekChange,
    reportDate,
}
