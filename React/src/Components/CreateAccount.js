import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Header from './Header';
import * as yup from 'yup';
import schema from '../validation';

const initialFormValues = {
    email: "",
    username: "",
    password: "",
};
export default function CreateAccount() {
    const [formValues, setFormValues] = useState(initialFormValues);
    const [errors, setErrors] = useState(initialFormValues);
    const [disabled, setDisabled] = useState(true);

    const validate = (name, value) => {
        yup.reach(schema, name)
            .validate(value)
            .then(() => setErrors({ ...errors, [name]: "" }))
            .catch(err => setErrors({ ...errors, [name]: err.errors[0] }));
    }
    const change = e => {
        const { name, value } = e.target;
        validate(name, value);
        setFormValues({...formValues, [name]: value });
        console.log(formValues);
    }
    const submit = e => {
        e.preventDefault()
        const newAccount = {
            email: formValues.email,
            username: formValues.username,
            password: formValues.password,
        }
        // Post
        setFormValues(initialFormValues);
    }
    useEffect(() => {
        schema.isValid(formValues)
            .then(valid => setDisabled(!valid));
    }, [formValues])
    return (
        <>
        <Header/>
        <form id="create-account-form" onSubmit={submit}>
            <label>
                <input 
                    type="email"
                    name="email"
                    onChange={change}
                    placeholder="phone"
                />
            </label>
            <label>
                <input 
                    type="text"
                    name="username"
                    onChange={change}
                    placeholder="username"
                />
            </label>
            <label>
                <input 
                    type="password"
                    name="password"
                    onChange={change}
                    placeholder="password"
                />
            </label>
            <Link to="/create-account">
                <button disabled={disabled}>Create</button>
            </Link>
        </form>
        </>
    )
}
