import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import App from './App'

const rootDiv = document.getElementById('root')

if (rootDiv !== null) {
  const root = ReactDOM.createRoot(rootDiv)
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
  )
}
