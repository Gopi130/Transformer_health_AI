import React, { useState } from "react";

function App() {
const inputStyle = {
  padding: "16px",
  borderRadius: "10px",
  border: "1px solid #374151",
  backgroundColor: "#111827",
  color: "white",
  fontSize: "16px",
  width: "100%"
};
  const [hydrogen, setHydrogen] = useState("");
  const [methane, setMethane] = useState("");
  const [ethylene, setEthylene] = useState("");
  const [ethane, setEthane] = useState("");
  const [acetylene, setAcetylene] = useState("");
  const [co, setCo] = useState("");
const [kv, setKv] = useState("");
const [ir, setIr] = useState("");

const [acid, setAcid] = useState("");
const [water, setWater] = useState("");
const [breakdown, setBreakdown] = useState("");
const [viscosity, setViscosity] = useState("");
  const [result, setResult] = useState("");

  const predictHealth = async () => {

    const response = await fetch("http://127.0.0.1:8000/predict", {

      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
  hydrogen: Number(hydrogen),
  methane: Number(methane),
  ethylene: Number(ethylene),
  ethane: Number(ethane),
  acetylene: Number(acetylene),
  co: Number(co)
})

    });

    const data = await response.json();

    setResult(data.condition);
  };

  return (
    

    <div style={{
      backgroundColor: "#0E1117",
      color: "white",
      minHeight: "100vh",
      padding: "40px"
    }}>

      <h1>⚡ SMART TRANSFORMER HEALTH AI SYSTEM</h1>

      <h2>DGA Analysis</h2>
<h2>⚡ IR Analysis</h2>

<input
  type="number"
  placeholder="KV Rating"
  value={kv}
  onChange={(e) => setKv(e.target.value)}
  style={inputStyle}
/>

<br /><br />

<input
  type="number"
  placeholder="IR Value"
  value={ir}
  onChange={(e) => setIr(e.target.value)}
  style={inputStyle}
/>

<br /><br />

<h2>⚡ DGA Analysis</h2>

<div
  style={{
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "15px",
    maxWidth: "900px"
  }}
>

  <input
    type="number"
    placeholder="Hydrogen"
    value={hydrogen}
    onChange={(e) => setHydrogen(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Methane"
    value={methane}
    onChange={(e) => setMethane(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Ethylene"
    value={ethylene}
    onChange={(e) => setEthylene(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Ethane"
    value={ethane}
    onChange={(e) => setEthane(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Acetylene"
    value={acetylene}
    onChange={(e) => setAcetylene(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Carbon Monoxide"
    value={co}
    onChange={(e) => setCo(e.target.value)}
    style={inputStyle}
  />

</div>

<br /><br />

<h2>🛢 Oil Parameters</h2>

<div
  style={{
    display: "grid",
    gridTemplateColumns: "1fr 1fr",
    gap: "15px",
    maxWidth: "900px"
  }}
>

  <input
    type="number"
    placeholder="Acid Number"
    value={acid}
    onChange={(e) => setAcid(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Water Content"
    value={water}
    onChange={(e) => setWater(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Breakdown Voltage"
    value={breakdown}
    onChange={(e) => setBreakdown(e.target.value)}
    style={inputStyle}
  />

  <input
    type="number"
    placeholder="Viscosity"
    value={viscosity}
    onChange={(e) => setViscosity(e.target.value)}
    style={inputStyle}
  />

</div>

<br /><br />
      <button
        onClick={predictHealth}
        style={{
          padding: "12px",
          backgroundColor: "cyan",
          border: "none",
          borderRadius: "10px",
          cursor: "pointer"
        }}
      >
        Predict Transformer Health
      </button>

      <h2>Prediction Result: {result}</h2>

    </div>
  );
}

export default App; 