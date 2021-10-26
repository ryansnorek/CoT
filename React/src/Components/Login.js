import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import Header from './Header';

const initialFormValues = {
    username: '',
    password: ''
};
export default function Login() {
    const [formValues, setFormValues] = useState(initialFormValues);

    const change = e => {
        const { name, value } = e.target;
        setFormValues({...formValues, [name]: value });
    }
    return (
        <>
        <Header/>
        <form id="login-form">
            <label>
                <input 
                    type="text"
                    name="username"
                    onChange={change}
                    placeholder='username'
                />
            </label>
            <label>
                <input 
                    type="text"
                    name="password"
                    onChange={change}
                    placeholder='password'
                />
            </label>
            <Link to="/profile">
                <button>Login</button>
            </Link>
        </form>
        <Link to="/create-account">
            <button className="create-button">Create Account</button>
        </Link>
        </>
    )
}
