export default function Content() {
  return (
    <div style={{padding:40}}>
      <h1>AI Content Generator</h1>

      <input
        placeholder="Enter topic"
        style={{padding:10,width:300}}
      />

      <button style={{marginLeft:10,padding:10}}>
        Generate Blog
      </button>

    </div>
  )
}
