from fastapi import FastAPI

# Existing Routers
from auth import router as auth_router
from website import router as website_router
from ai_content import router as content_router
from seo_audit import router as seo_router
from growth_agent import router as growth_router

# New SEO AI Modules
from keyword_engine import router as keyword_router
from blog_generator import router as blog_router
from seo_score import router as seo_score_router
from backlink_finder import router as backlink_router
from autorank_engine import router as autorank_router
from ai_writer import router as ai_router
from competitor_engine import router as competitor_router
from technical_seo import router as technical_router
from strategy_engine import router as strategy_router
from link_building import router as link_router
from analytics_engine import router as analytics_router
from master_agent import router as agent_router
from subscription import router as sub_router
from crawler_engine import router as crawler_router
from rank_tracker import router as rank_router
from keyword_difficulty import router as kd_router
from backlink_database import router as backlink_db_router
from content_optimizer import router as optimizer_router
from report_generator import router as report_router
from project_manager import router as project_router
from team_system import router as team_router
from notification_system import router as notification_router

app = FastAPI(
    title="RankPilot AI",
    description="AI SEO Agent + AI Traffic Growth System",
    version="1.0"
)

# Core Routers
app.include_router(auth_router)
app.include_router(website_router)
app.include_router(content_router)
app.include_router(seo_router)
app.include_router(growth_router)
app.include_router(autorank_router)
app.include_router(ai_router)
app.include_router(competitor_router)
app.include_router(technical_router)
app.include_router(strategy_router)
app.include_router(link_router)
app.include_router(analytics_router)
app.include_router(agent_router)
app.include_router(sub_router)
app.include_router(crawler_router)
app.include_router(rank_router)
app.include_router(kd_router)
app.include_router(backlink_db_router)
app.include_router(optimizer_router)
app.include_router(report_router)
app.include_router(project_router)
app.include_router(team_router)
app.include_router(notification_router)

# AI SEO Tools
app.include_router(keyword_router)
app.include_router(blog_router)
app.include_router(seo_score_router)
app.include_router(backlink_router)


@app.get("/")
def home():
    return {
        "message": "RankPilot AI running",
        "modules": [
            "Auth System",
            "Website Manager",
            "AI Content Generator",
            "SEO Audit Engine",
            "Growth Agent",
            "Keyword Engine",
            "Blog Generator",
            "SEO Score Analyzer",
            "Backlink Finder"
        ]
    }
