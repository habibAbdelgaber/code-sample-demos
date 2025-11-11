/* import React, { useState } from 'react';

const Login = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = () => {
        if (username === 'admin' && email === 'admin@gmail.com' && password === 'admin12345') {
            localStorage.setItem('user', JSON.stringify({ username, email }));
            alert('Login successful!');
        } else {
            setError('Invalid credentials!');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <input 
                type="text" 
                placeholder="Username" 
                value={username} 
                onChange={(e) => setUsername(e.target.value)} 
            />
            <input 
                type="email" 
                placeholder="Email" 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
            />
            <input 
                type="password" 
                placeholder="Password" 
                value={password} 
                onChange={(e) => setPassword(e.target.value)} 
            />
            <button onClick={handleLogin}>Login</button>
        </div>
    );
};

export default Login;
*/
import React, { useState } from 'react';

const DEMO_CREDENTIAL = {
  username: "admin",
  email: "admin@gmail.com",
  password: "admin12345",
};

const styles = {
  container: {
    maxWidth: 400,
    margin: "60px auto",
    padding: 32,
    borderRadius: 12,
    boxShadow: "0 6px 24px rgba(0,0,0,0.13)",
    backgroundColor: "#fff",
    fontFamily: "Arial,sans-serif"
  },
  title: {
    fontWeight: 700,
    fontSize: 24,
    textAlign: "center",
    marginBottom: 24,
    letterSpacing: "1px",
    color: "#222",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: 16,
  },
  input: {
    padding: "10px 12px",
    fontSize: 16,
    border: "1px solid #ddd",
    borderRadius: 7,
    outline: "none",
    transition: "border 0.2s",
  },
  button: {
    padding: "10px",
    background: "linear-gradient(90deg,#3578b4 60%,#295096 100%)",
    color: "#fff",
    border: "none",
    fontSize: 17,
    borderRadius: 7,
    cursor: "pointer",
    fontWeight: 600,
    letterSpacing: "2px"
  },
  error: {
    color: "#be3144",
    background: "#ffecef",
    padding: "10px",
    borderRadius: 7,
    fontSize: 15,
    textAlign: "center",
  },
  success: {
    color: "#2c8d45",
    background: "#e3ffe3",
    padding: "10px",
    borderRadius: 7,
    fontSize: 15,
    textAlign: "center",
  }
};

function Login() {
  const [state, setState] = useState({
    username: "",
    email: "",
    password: "",
  });
  const [err, setErr] = useState("");
  const [success, setSuccess] = useState("");

  function handleInput(e) {
    setState({ ...state, [e.target.name]: e.target.value });
    setErr("");
    setSuccess("");
  }

  function onSubmit(e) {
    e.preventDefault();
    setErr("");
    setSuccess("");
    // Check credentials
    if (
      state.username === DEMO_CREDENTIAL.username &&
      state.email === DEMO_CREDENTIAL.email &&
      state.password === DEMO_CREDENTIAL.password
    ) {
      // Save to localStorage
      localStorage.setItem("demoUser", JSON.stringify({
        username: state.username,
        email: state.email,
      }));
      setSuccess("Login successful! Welcome, admin.");
      setState({ username: "", email: "", password: "" });
    } else {
      setErr("Invalid credentials! Try with: admin, admin@gmail.com, admin12345.");
    }
  }

  return (
    <div style={styles.container}>
      <div style={styles.title}>Demo Admin Login</div>
      <form style={styles.form} autoComplete="off" onSubmit={onSubmit}>
        <input
          style={styles.input}
          name="username"
          value={state.username}
          onChange={handleInput}
          placeholder="Username"
        />
        <input
          style={styles.input}
          name="email"
          value={state.email}
          onChange={handleInput}
          type="email"
          placeholder="Email"
        />
        <input
          style={styles.input}
          name="password"
          value={state.password}
          onChange={handleInput}
          type="password"
          placeholder="Password"
        />
        <button style={styles.button} type="submit">Login</button>
      </form>
      {err && <div style={styles.error}>{err}</div>}
      {success && <div style={styles.success}>{success}</div>}
      <div style={{marginTop:20, fontSize:13, color:"#888"}}>
        <b>Demo Credentials:</b>
        <div>Username: admin</div>
        <div>Email: admin@gmail.com</div>
        <div>Password: admin12345</div>
      </div>
    </div>
  );
}

export default Login;
