import { useState } from 'react';
import './css/styles.css'
import Menu from './Menu';

const LogInPage = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError("")

        try {
            const response = await fetch("http://127.0.0.1:8000/api/token/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({username, password}),
            })

            const data = await response.json();

            if (response.ok) {
                localStorage.setItem('access_token', data.access);
                localStorage.setItem('refresh_token', data.refresh);
                // Set authorization header for future fetch requests
                setAuthHeader();
                console.log("Logged In Successfully")
            } else {
                const errorData = await response.json()
                setError(errorData.message || "Login Failed")
            }
        } catch (error) {
            setError("An error occurred. Please Try Again!")
        }
    }

    const setAuthHeader = () => {
        const token = localStorage.getItem('access_token');
        if (token) {
            fetch.defaults = {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }
        }
    }

    return (
        <div>
            < Menu />
            <div style={styles.container}>
                <h2>Login</h2>
                {error && <p style={styles.error}>{error}</p>}
                <form onSubmit={handleSubmit} style={styles.form}>
                    <div style={styles.formGroup}>
                    <label>Username</label>
                    <input
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        style={styles.input}
                        placeholder="Enter your email"
                    />
                    </div>
                    <div style={styles.formGroup}>
                    <label>Password</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        style={styles.input}
                        placeholder="Enter your password"
                    />
                    </div>
                    <button type="submit" style={styles.button}>
                    Login
                    </button>
                </form>

            </div>

        </div>
    )
};

const styles = {
    container: {
      maxWidth: "400px",
      margin: "0 auto",
      padding: "20px",
      border: "1px solid #ccc",
      borderRadius: "5px",
      textAlign: "center",
    },
    form: {
      display: "flex",
      flexDirection: "column",
    },
    formGroup: {
      marginBottom: "15px",
    },
    input: {
      padding: "10px",
      fontSize: "16px",
      width: "100%",
      marginBottom: "10px",
      borderRadius: "4px",
      border: "1px solid #ccc",
    },
    button: {
      padding: "10px",
      fontSize: "16px",
      backgroundColor: "#007BFF",
      color: "#fff",
      border: "none",
      borderRadius: "4px",
      cursor: "pointer",
    },
    error: {
      color: "red",
    },
  };

export default LogInPage;