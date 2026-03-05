"use client"

import { useEffect, useState } from "react"

export default function Home() {

  const [data, setData] = useState(null)

  useEffect(() => {

    fetch(process.env.NEXT_PUBLIC_API + "/dashboard?domain=example.com")
      .then(res => res.json())
      .then(data => setData(data))

  }, [])

  if (!data) return <div>Loading...</div>

  return (
    <div className="p-10">

      <h1 className="text-3xl font-bold">RankPilot AI Dashboard</h1>

      <div className="grid grid-cols-2 gap-4 mt-6">

        <div className="p-4 bg-gray-100">
          SEO Score: {data.seo_score}
        </div>

        <div className="p-4 bg-gray-100">
          Keywords Ranked: {data.keywords_ranked}
        </div>

        <div className="p-4 bg-gray-100">
          Backlinks: {data.backlinks}
        </div>

        <div className="p-4 bg-gray-100">
          Traffic: {data.traffic_estimate}
        </div>

      </div>

      <div className="mt-6 p-4 bg-blue-100">
        AI Suggestion: {data.ai_suggestion}
      </div>

    </div>
  )
}
