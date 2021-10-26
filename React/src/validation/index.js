import * as yup from 'yup';

const createAccountSchema = yup.object().shape({
    email: yup
        .string()
        .email("Must be a valid email")
        .required("Email required"),
    username: yup
        .string()
        .trim()
        .min(3, 'Username must have at least 3 characters')
        .required('Username required'),
    password: yup
        .string()
        .trim()
        .min(6, 'Password must have at least 6 characters')
        .required('Password required')
})

export default createAccountSchema;