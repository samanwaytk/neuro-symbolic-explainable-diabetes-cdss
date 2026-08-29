function ShapExplanation({ shapData }) {
  if (!shapData) {
    return null
  }

  const features = Object.entries(shapData)

  return (
    <div className="shap-card">
      <h2>AI Explainability</h2>

      <p className="shap-description">
        SHAP shows how each patient feature influenced the diabetes prediction.
      </p>

      <div className="shap-list">
        {features
          .sort((a, b) => Math.abs(b[1].impact) - Math.abs(a[1].impact))
          .map(([feature, data]) => (
            <div className="shap-row" key={feature}>

              <div className="shap-feature">
                {feature}
              </div>

              <div className="shap-bar-container">
                <div
                  className={`shap-bar ${
                    data.impact >= 0 ? "positive" : "negative"
                  }`}
                  style={{
                    width: `${Math.min(Math.abs(data.impact) * 100, 100)}%`
                  }}
                />
              </div>

              <div className="shap-value">
                {data.impact >= 0 ? "+" : ""}
                {data.impact.toFixed(3)}
              </div>

              <div
                className={`shap-direction ${
                  data.impact >= 0 ? "risk" : "protective"
                }`}
              >
                {data.direction}
              </div>

            </div>
          ))}
      </div>
    </div>
  )
}

export default ShapExplanation