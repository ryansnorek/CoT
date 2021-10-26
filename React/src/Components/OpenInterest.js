import React from 'react';
import { data } from '../helper/data';
import { format } from '../helper/format';
import { icons } from '../assets/icons';

export default function OpenInterest({ cot, cotData }) {
    return ( 
        <>
        <h4 className="title">{cot.title}</h4>
            <div className="section">
                <div className="data">
                    <p>Open Interest: {cot.oi.toLocaleString()}</p>
                    <p>Week change: {format.weekChange(cot.oiChange)}</p>
                    <p>Average: {cotData[cot.name] ? 
                       cotData[cot.name]["Open_Interest_All"].mean.toLocaleString() 
                       : "unavailable"}
                    </p>
                    <p>Deviation: {cotData[cot.name] ? 
                        data.deviation(cot.oi, cotData[cot.name]["Open_Interest_All"])
                        : "unavailable"} 
                    </p>
                </div>
                <img className="icon" src={icons[cot.code] ? icons[cot.code].img : ''} alt={icons[cot.code] ? icons[cot.code].name : ''}></img>
            </div> 
        </>
    )
        
      
}
