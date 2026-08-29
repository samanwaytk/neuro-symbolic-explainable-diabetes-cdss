function ResultCard({ result }) {


if (!result) {

    return (
        <div className="result-card">

            <h2>
                Prediction Result
            </h2>

            <p>
                Waiting for assessment...
            </p>

        </div>
    )

}


return (

<div className="result-container">


<div className="risk-card">

<h2>
{result.final_decision}
</h2>


<div className="confidence">

Confidence

<h1>
{(result.probability * 100).toFixed(2)}%
</h1>

</div>


</div>



<div className="info-card">

<h3>
🧠 Symbolic Risk Analysis
</h3>


<ul>

{
result.reasons.map((reason,index)=>(

<li key={index}>
{reason}
</li>

))

}

</ul>


</div>




<div className="info-card">


<h3>
🤖 AI Clinical Explanation
</h3>


<p>
{result.llm_explanation}
</p>


</div>



</div>

)

}


export default ResultCard;