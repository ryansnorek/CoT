const cleanUp = (data) => {
    data = data.split("\n").map(row => row.split(","))
    // Field names to be used for keys
    let fields = ["Market_and_Exchange_Names","As_of_Date_In_Form_YYMMDD","Report_Date_as_YYYY-MM-DD","CFTC_Contract_Market_Code","CFTC_Market_Code","CFTC_Region_Code","CFTC_Commodity_Code","Open_Interest_All","Dealer_Positions_Long_All","Dealer_Positions_Short_All","Dealer_Positions_Spread_All","Asset_Mgr_Positions_Long_All","Asset_Mgr_Positions_Short_All","Asset_Mgr_Positions_Spread_All","Lev_Money_Positions_Long_All","Lev_Money_Positions_Short_All","Lev_Money_Positions_Spread_All","Other_Rept_Positions_Long_All","Other_Rept_Positions_Short_All","Other_Rept_Positions_Spread_All","Tot_Rept_Positions_Long_All","Tot_Rept_Positions_Short_All","NonRept_Positions_Long_All","NonRept_Positions_Short_All","Change_in_Open_Interest_All","Change_in_Dealer_Long_All","Change_in_Dealer_Short_All","Change_in_Dealer_Spread_All","Change_in_Asset_Mgr_Long_All","Change_in_Asset_Mgr_Short_All","Change_in_Asset_Mgr_Spread_All","Change_in_Lev_Money_Long_All","Change_in_Lev_Money_Short_All","Change_in_Lev_Money_Spread_All","Change_in_Other_Rept_Long_All","Change_in_Other_Rept_Short_All","Change_in_Other_Rept_Spread_All","Change_in_Tot_Rept_Long_All","Change_in_Tot_Rept_Short_All","Change_in_NonRept_Long_All","Change_in_NonRept_Short_All","Pct_of_Open_Interest_All","Pct_of_OI_Dealer_Long_All","Pct_of_OI_Dealer_Short_All","Pct_of_OI_Dealer_Spread_All","Pct_of_OI_Asset_Mgr_Long_All","Pct_of_OI_Asset_Mgr_Short_All","Pct_of_OI_Asset_Mgr_Spread_All","Pct_of_OI_Lev_Money_Long_All","Pct_of_OI_Lev_Money_Short_All","Pct_of_OI_Lev_Money_Spread_All","Pct_of_OI_Other_Rept_Long_All","Pct_of_OI_Other_Rept_Short_All","Pct_of_OI_Other_Rept_Spread_All","Pct_of_OI_Tot_Rept_Long_All","Pct_of_OI_Tot_Rept_Short_All","Pct_of_OI_NonRept_Long_All","Pct_of_OI_NonRept_Short_All","Traders_Tot_All","Traders_Dealer_Long_All","Traders_Dealer_Short_All","Traders_Dealer_Spread_All","Traders_Asset_Mgr_Long_All","Traders_Asset_Mgr_Short_All","Traders_Asset_Mgr_Spread_All","Traders_Lev_Money_Long_All","Traders_Lev_Money_Short_All","Traders_Lev_Money_Spread_All","Traders_Other_Rept_Long_All","Traders_Other_Rept_Short_All","Traders_Other_Rept_Spread_All","Traders_Tot_Rept_Long_All","Traders_Tot_Rept_Short_All","Conc_Gross_LE_4_TDR_Long_All","Conc_Gross_LE_4_TDR_Short_All","Conc_Gross_LE_8_TDR_Long_All","Conc_Gross_LE_8_TDR_Short_All","Conc_Net_LE_4_TDR_Long_All","Conc_Net_LE_4_TDR_Short_All","Conc_Net_LE_8_TDR_Long_All","Conc_Net_LE_8_TDR_Short_All","Contract_Units","CFTC_Contract_Market_Code_Quotes","CFTC_Market_Code_Quotes","CFTC_Commodity_Code_Quotes","CFTC_SubGroup_Code","FutOnly_or_Combined"]
    // Store full report in cot object
    const cot = {};
    // Create an object for each section
    data.forEach((section, idx) => {
    const cotSection = {};
        // Assign field name key to each value in the section
        section.forEach((el, i) => {
            cotSection[fields[i]] = el;
            // Append section object to cot object
            cot[idx] = cotSection;
        })
    })
    // Clean cot data and push only what is needed to new array
    const cleanCot = [];
    for (let key in cot) {
        const cleanCotObj = {};
        cleanCotObj['name'] = cot[key][fields[0]].replace('"','').replace('"','');
        cleanCotObj['title'] = cot[key][fields[0]].replace('"','').replace('CHICAGO','').replace('MERCANTILE','').replace('EXCHANGE','').replace('-','').replace('"','').replace('BOARD OF TRADE','').replace('x $5 -','').replace('-','').replace('-','');
        cleanCotObj['date'] = cot[key][fields[2]];
        cleanCotObj['code'] = cot[key][fields[3]];
        cleanCotObj['oi'] = Number(cot[key][fields[7]]);
        cleanCotObj['amLong'] = Number(cot[key][fields[11]]);
        cleanCotObj['amShort'] = Number(cot[key][fields[12]]);
        cleanCotObj['levLong'] = Number(cot[key][fields[14]]);
        cleanCotObj['levShort'] = Number(cot[key][fields[15]]);
        cleanCotObj['oiChange'] = Number(cot[key][fields[24]]);
        cleanCotObj['amLongChange'] = Number(cot[key][fields[28]]);
        cleanCotObj['amShortChange'] = Number(cot[key][fields[29]]);
        cleanCotObj['levLongChange'] = Number(cot[key][fields[31]]);
        cleanCotObj['levShortChange'] = Number(cot[key][fields[32]]);
        cleanCot.push(cleanCotObj);
    }
    cleanCot.pop();
    return cleanCot;
}
const analyze = (report, metrics) => {
    const history = metrics['cot2020']
    // Isolate the names
    const reportNames = report.map(el => el.name);
    const historyNames = history[0].map(el => el.name);
    // Find matching names in DB
    const matchingNames = [];
    reportNames.forEach(name => {
        if (historyNames.includes(name)) {
            matchingNames.push(name)
        }
    })
    // Consolidate all metrics by name 
    const positionsObj = {};
    const traderMetrics = {};
    matchingNames.forEach(name => {
        history.forEach(position => {
            position.forEach(item => {
                let column = item.column;
                if (name === item.name) {
                    positionsObj[column] = { 
                                                "max": item.max,
                                                "min": item.min,
                                                "mean": item.mean,
                                                "median": item.median
                                            };
                }
            })
            traderMetrics[name] = { ...traderMetrics[name], ...positionsObj};
        })
    })
    return traderMetrics;
}
const deviation = (current, metrics) => {
    function percentChange(current, average) {
        if (current === 0) {
            return -100 + '% ';
        }
        else if (average === 0) {
            return 100 + '% ';
        }
        let change = ((current - average) / average * 100).toFixed(2);
        return change + '% ';
    }
    return percentChange(current, metrics.mean).toLocaleString()
}
const historyMetrics = (db, year) => {
    const metrics = {}
    function organizeData() {
        // Get only the asset name from each line and store in an array called [assetNames]
        let assetNames = db.map(line => line["Market_and_Exchange_Names"]);
        // Remove duplicates 
        assetNames = [...new Set(assetNames)];
        // Gather all the weekly report data by asset name and store in an array called [dataArray]
        const filterByName = name => db.filter(line => line["Market_and_Exchange_Names"] === name);
        const dataArray = assetNames.map(name => filterByName(name));
        // Return an object with the asset names as keys and all the asset's data as values
        const dataObj = {};
        dataArray.forEach((data, i) => dataObj[assetNames[i]] = data);
        return dataObj;
    }
    const data = organizeData();
    const names = Object.keys(data);
    // Takes in asset name and the column to pull data from. Then returns median, mean, min, max for the entire data set.
    function getStatsByName(name, column) {
        const values = data[name].map(report => report[column]);
        values.sort((a, b) => a - b);
        const half = Math.floor(values.length / 2);
        let median = values[half];
        const mean = Math.floor(
                        data[name]
                        .reduce((acc, line) => acc += line[`${column}`], 0)
                         / data[name].length
                         );
        const min = values[0];
        const max = values[values.length - 1];
        // Handle odd numbers
        if (!values.length % 2) median = (values[half - 1] + values[half]) / 2.0;
        return { name, column, median, mean, min, max };
    }
    // Grab only the columns that are useful for pulling stats out of
    const columns = Object.keys(db[0]);
    const metricsColumns = columns.slice(3, 14);
    // Map an array that contains every asset name with a complete list of stats from each column
    const allMetrics = metricsColumns.map(column => {
        return names.map(name => getStatsByName(name, column));
    })
    metrics[year] = allMetrics;
    return metrics;
}

export const data = {
    cleanUp,
    analyze,
    deviation,
    historyMetrics,
}