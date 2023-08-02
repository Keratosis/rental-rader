import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import '../CSS/login.css';

const validationSchema = Yup.object().shape({
  email: Yup.string().email('Invalid email address').required('Email is required'),
  password: Yup.string().required('Password is required'),
});

function Login() {
  const handleSubmit = async (values, { setSubmitting, setStatus }) => {
    try {
      const response = await fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: values.email,
          password: values.password,
        }),
      });

      if (!response.ok) {
        const data = await response.json();
        setStatus(data.message); // Set the server error message in the 'status' variable
        setSubmitting(false);
        return;
      }

      const data = await response.json();
      // Assuming the server returns an access token after successful login
      localStorage.setItem('access_token', data.access_token);
      // Navigate to the home page after successful login
      window.location.href = '/'; // Change this to the appropriate home page path
    } catch (error) {
      console.error('Error during login:', error);
      setStatus('An error occurred during login.'); // Generic error message for other errors
      setSubmitting(false);
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <Formik
        initialValues={{
          email: '',
          password: '',
        }}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ isSubmitting, status }) => (
          <Form>
            {/* Display server-side error if present */}
            {status && <div className="error">{status}</div>}

            <div className="form-group">
              <label htmlFor="email">Email</label>
              <Field type="email" id="email" name="email" required />
              <ErrorMessage name="email" component="div" className="error" />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <Field type="password" id="password" name="password" required />
              <ErrorMessage name="password" component="div" className="error" />
            </div>
            <button type="submit" disabled={isSubmitting}>
              Login
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
}

export default Login;
