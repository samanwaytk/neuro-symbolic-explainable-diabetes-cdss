import { useState } from "react";
import ShapExplanation from "./components/ShapExplanation";
import PatientForm from "./components/PatientForm";
import ResultCard from "./components/ResultCard";

import "./App.css";


function App(){


const [result,setResult] = useState(null);



return (

<div className="container">


<h1>
Neuro-Symbolic XAI CDSS
</h1>


<PatientForm setResult={setResult}/>
{result?.shap_explanation && (
  <ShapExplanation
    shapData={result.shap_explanation}
  />
)}


<ResultCard result={result}/>


</div>

)

}


export default App;