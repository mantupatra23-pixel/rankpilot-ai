export default function Dashboard() {
  return (
    <div style={{padding:40}}>
      <h1>RankPilot AI Dashboard</h1>

      <div style={{display:"grid",gridTemplateColumns:"repeat(2,1fr)",gap:20,marginTop:30}}>

        <a href="/audit">
          <div style={{border:"1px solid #ddd",padding:20}}>
            <h2>SEO Audit</h2>
            <p>Analyze your website SEO</p>
          </div>
        </a>

        <a href="/keywords">
          <div style={{border:"1px solid #ddd",padding:20}}>
            <h2>Keyword Research</h2>
            <p>Find ranking keywords</p>
          </div>
        </a>

        <a href="/backlinks">
          <div style={{border:"1px solid #ddd",padding:20}}>
            <h2>Backlink Builder</h2>
            <p>Create backlinks automatically</p>
          </div>
        </a>

        <a href="/content">
          <div style={{border:"1px solid #ddd",padding:20}}>
            <h2>AI Content Generator</h2>
            <p>Create SEO blog posts</p>
          </div>
        </a>

      </div>
    </div>
  )
}
