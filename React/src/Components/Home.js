import { Link } from 'react-router-dom';
import React from 'react';

export default function Home() {

    return (
        <header className="App-header">
            <h1>Cot ~tails</h1>
            <p className="follow">Follow the money</p>
            <Link to="/report" className="glow App-launch" >Launch</Link>
        </header>
    )
}