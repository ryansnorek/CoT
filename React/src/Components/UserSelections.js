import React from 'react';
import { format } from '../helper/format';

export default function UserSelections({ report, change, year, deviation }) {
    return (
        <>
        <div className="date">
            {typeof report[0] != "undefined" ? 
            <p>Traders in Financial Futures as of {format.reportDate(report[0].date)}</p> 
            : ''}
        </div>
        <div className="user-inputs">
            <div className="text">
                <p>Comparing averages from</p>
                <p>Deviation from average</p>
            </div>
            <div className="user-select">
                <select 
                    className="dropdown"
                    value={year}
                    onChange={change}
                >
                    <option value="cot2020">2020</option>
                    <option value="cot2019">2019</option>
                    <option value="cot2018">2018</option>
                    <option value="cot2017">2017</option>
                    <option value="cot2016">2016</option>
                    <option value="5yraverage">5yr Average</option>
                </select>
                <select 
                    className="dropdown"
                    value={deviation}
                    onChange={change}
                >
                    <option value={0}>%</option>
                    <option value={200}>200%</option>
                    <option value={150}>150%</option>
                    <option value={125}>125%</option>
                    <option value={100}>100%</option>
                    <option value={75}>75%</option>
                    <option value={50}>50%</option>
                    <option value={25}>25%</option>
                </select>
            </div>
          
        </div>
        


        {/* <div className="user-select">
            <p>Comparing averages from</p>
            <select 
                className="dropdown"
                value={year}
                onChange={change}
            >
                <option value="cot2020">2020</option>
                <option value="cot2019">2019</option>
                <option value="cot2018">2018</option>
                <option value="cot2017">2017</option>
                <option value="cot2016">2016</option>
                <option value="5yraverage">5yr Average</option>
            </select>
        </div>
        <div className="user-select">
            <p>Deviation from average</p>
            <select 
                className="dropdown"
                value={deviation}
                onChange={change}
            >
                <option value={0}>%</option>
                <option value={200}>200%</option>
                <option value={150}>150%</option>
                <option value={125}>125%</option>
                <option value={100}>100%</option>
                <option value={75}>75%</option>
                <option value={50}>50%</option>
                <option value={25}>25%</option>
            </select>
        </div> */}
        </>
    )
}
