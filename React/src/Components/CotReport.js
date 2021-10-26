import { useState, useEffect } from 'react';
import axios from 'axios';
import { data } from '../helper/data';
import Header from './Header';
import OpenInterest from './OpenInterest';
import Trader from './Trader';
import UserSelections from './UserSelections';

export default function CotReport() {
    const [report, setReport] = useState([]);
    const [loadingReport, setLoadingReport] = useState(false);
    const [metrics, setMetrics] = useState([]);
    const [loadingMetrics, setLoadingMetrics] = useState(false);
    const [year, setYear] = useState('cot2020');
    const [deviation, setDeviation] = useState("");
    const [cotData, setCotData] = useState({});
    const [errors, setErrors] = useState();

    const change = (e) => {
        const { value } = e.target;
        if (typeof value === 'string') setYear(value)
        else setDeviation(value)
    }
    // CURRENT REPORT //
    useEffect(() => {
        setLoadingReport(true)
        axios.get('/dea/newcot/FinFutWk.txt')
            .then(res => {
                const cleanReport = data.cleanUp(res.data)
                setReport(cleanReport)
            })
            .catch(err => setErrors(err))
            .finally(() => setLoadingReport(false)); 
         },[])
    // COT HISTORY //
    useEffect(() => {
        setLoadingMetrics(true)
        axios.get('http://localhost:3000/api/v1/cothistory')
            .then(res => {
                const historyMetrics = data.historyMetrics(res.data, year);
                    setMetrics(historyMetrics);
            })
            .catch(err => setErrors(err))
            .finally(() => setLoadingMetrics(false))
    }, [year])
    // CURRENT REPORT VS HISTORY
    useEffect(() => {
        if (typeof metrics['cot2020'] === "object") {
            const d = data.analyze(report, metrics)
            setCotData(d);
        }
    }, [loadingMetrics])
    
    // DEVIATION PERCENT CHANGE //
    // useEffect(() => {
    //     const d = filterByDeviation(report, metrics);
    //     setCotData(d)
    // }, [deviation])
    if (loadingReport || loadingMetrics) {
        return (
            <>
            <Header/>
            <h1 styles={"margin-left: 50%"}>loading...</h1>
            </>
        )
    }
    return (
        <>
        <Header/>
        <div className="report">
            <div className="top">
                <UserSelections 
                    report={report}
                    change={change}
                    year={year}
                    deviation={deviation}
                />
            </div>
            {report.map(cot => (
                <>
                <OpenInterest cot={cot} cotData={cotData}/>
                <Trader traderName="Asset Managers" cot={cot} cotData={cotData}/>
                <Trader traderName="Hedge Funds" cot={cot} cotData={cotData}/>
                </>
            ))}
        </div>
        </>
    )
}
