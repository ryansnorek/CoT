import React from 'react';
import { format } from '../helper/format';
import { data } from '../helper/data';
 
export default function Trader({ traderName, cot, cotData }) {
    let n, x = "";
    if (traderName === "Asset Managers") {
        n = "am";
        x = "Asset_Mgr";
    }
    else if (traderName === "Hedge Funds") {
        n = "lev";
        x = "Lev_Money";
    }
    return (
        <>
        <h3 className="trader">{traderName}</h3>
        <div className="section">
            <div className="data">
                <p>Long: {cot[`${n}Long`].toLocaleString()}</p>
                <p>Week change: {format.weekChange(cot[`${n}LongChange`])}</p>
                <p>Average: {cotData[cot.name] ? 
                    cotData[cot.name][`${x}_Positions_Long_All`].mean.toLocaleString()
                    : "unavailable"}</p>
                <p>Deviation: {cotData[cot.name] ? 
                    data.deviation(cot[`${n}Long`], cotData[cot.name][`${x}_Positions_Long_All`])
                    : "unavailable"}
                </p>
            </div>
            <div className="data">
                <p>Short: {cot[`${n}Short`].toLocaleString()}</p>
                <p>Week change: {format.weekChange(cot[`${n}ShortChange`])}</p>
                <p>Average: {cotData[cot.name] ? 
                    cotData[cot.name][`${x}_Positions_Short_All`].mean.toLocaleString()
                    : "unavailable"}</p>
                <p>Deviation: {cotData[cot.name] ? 
                    data.deviation(cot[`${n}Short`], cotData[cot.name][`${x}_Positions_Short_All`])
                    : "unavailable"}
                </p>
            </div>
        </div>
        </>
    )
}
