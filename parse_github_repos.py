#!/usr/bin/env python3
"""
GitHub API Repository Parser
Extracts Top 10 projects and generates business insights
"""

import json
import requests
from datetime import datetime
from typing import List, Dict, Any

class GitHubRepoAnalyzer:
    def __init__(self):
        self.base_url = "https://api.github.com"
    
    def get_top_repositories(self, language: str = None, sort: str = "stars", 
                           direction: str = "desc", per_page: int = 10) -> List[Dict]:
        """Fetch top repositories from GitHub API"""
        url = f"{self.base_url}/repositories"
        params = {
            "sort": sort,
            "direction": direction,
            "per_page": per_page
        }
        if language:
            params["language"] = language
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching repositories: {e}")
            return []
    
    def extract_repo_data(self, repos: List[Dict]) -> List[Dict]:
        """Extract key fields from repository data"""
        extracted = []
        for repo in repos:
            extracted.append({
                "name": repo.get("name", ""),
                "full_name": repo.get("full_name", ""),
                "stars": repo.get("stargazers_count", 0),
                "language": repo.get("language", ""),
                "description": repo.get("description", "") or "",
                "url": repo.get("html_url", "")
            })
        return extracted
    
    def generate_business_insights(self, repos_data: List[Dict]) -> Dict[str, Any]:
        """Generate business insights from repository data"""
        insights = {
            "analysis_date": datetime.now().isoformat(),
            "total_repos": len(repos_data),
            "technical_direction": self._analyze_tech_direction(repos_data),
            "activity_analysis": self._analyze_activity(repos_data),
            "risk_assessment": self._assess_risks(repos_data)
        }
        return insights
    
    def _analyze_tech_direction(self, repos_data: List[Dict]) -> Dict[str, Any]:
        """Analyze technology direction based on languages"""
        language_count = {}
        for repo in repos_data:
            lang = repo["language"]
            if lang:
                language_count[lang] = language_count.get(lang, 0) + 1
        
        total = sum(language_count.values())
        language_distribution = {
            lang: {"count": count, "percentage": round(count/total*100, 2)}
            for lang, count in sorted(language_count.items(), key=lambda x: x[1], reverse=True)
        }
        
        dominant_language = max(language_count, key=language_count.get) if language_count else "N/A"
        
        return {
            "dominant_language": dominant_language,
            "language_distribution": language_distribution,
            "tech_trends": self._identify_tech_trends(repos_data)
        }
    
    def _identify_tech_trends(self, repos_data: List[Dict]) -> List[str]:
        """Identify technology trends based on repository names and descriptions"""
        trends = set()
        trending_keywords = [
            "machine learning", "ai", "deep learning", "neural", "nlp",
            "web framework", "api", "microservice", "container", "kubernetes",
            "blockchain", "crypto", "database", "orm", "frontend", "backend"
        ]
        
        for repo in repos_data:
            name_lower = repo["name"].lower()
            desc_lower = repo["description"].lower() if repo["description"] else ""
            
            for keyword in trending_keywords:
                if keyword in name_lower or keyword in desc_lower:
                    trends.add(keyword)
        
        return sorted(list(trends))
    
    def _analyze_activity(self, repos_data: List[Dict]) -> Dict[str, Any]:
        """Analyze repository activity"""
        star_distribution = {
            "high": 0,  # > 1000 stars
            "medium": 0,  # 100-1000 stars
            "low": 0  # < 100 stars
        }
        
        for repo in repos_data:
            stars = repo["stars"]
            if stars > 1000:
                star_distribution["high"] += 1
            elif stars >= 100:
                star_distribution["medium"] += 1
            else:
                star_distribution["low"] += 1
        
        avg_stars = sum(r["stars"] for r in repos_data) / len(repos_data) if repos_data else 0
        
        return {
            "star_distribution": star_distribution,
            "average_stars": round(avg_stars, 2),
            "popularity_score": self._calculate_popularity_score(repos_data)
        }
    
    def _calculate_popularity_score(self, repos_data: List[Dict]) -> str:
        """Calculate overall popularity score"""
        total_stars = sum(r["stars"] for r in repos_data)
        avg_stars = total_stars / len(repos_data) if repos_data else 0
        
        if avg_stars > 10000:
            return "High"
        elif avg_stars > 1000:
            return "Medium-High"
        elif avg_stars > 100:
            return "Medium"
        else:
            return "Low"
    
    def _assess_risks(self, repos_data: List[Dict]) -> List[Dict]:
        """Assess potential risks"""
        risks = []
        
        for repo in repos_data:
            risk_factors = []
            
            # Check for abandoned projects (no description)
            if not repo["description"]:
                risk_factors.append("No description - unclear purpose")
            
            # Check for low star count (might indicate low adoption)
            if repo["stars"] < 100:
                risk_factors.append("Low star count - limited adoption")
            
            # Check for generic names
            if len(repo["name"]) < 3:
                risk_factors.append("Generic name - unclear branding")
            
            if risk_factors:
                risks.append({
                    "repo": repo["full_name"],
                    "risks": risk_factors
                })
        
        return risks
    
    def run_analysis(self) -> Dict[str, Any]:
        """Run complete analysis"""
        print("Fetching top 10 repositories from GitHub...")
        repos = self.get_top_repositories()
        
        if not repos:
            return {"error": "No repositories fetched"}
        
        print(f"Fetched {len(repos)} repositories")
        
        repos_data = self.extract_repo_data(repos)
        insights = self.generate_business_insights(repos_data)
        
        return {
            "metadata": {
                "extracted_at": datetime.now().isoformat(),
                "source": "GitHub API"
            },
            "repositories": repos_data,
            "insights": insights
        }

def main():
    analyzer = GitHubRepoAnalyzer()
    result = analyzer.run_analysis()
    
    # Print formatted results
    print("\n" + "="*80)
    print("GITHUB REPOSITORY ANALYSIS REPORT")
    print("="*80)
    
    if "error" in result:
        print(f"Error: {result['error']}")
        return
    
    metadata = result["metadata"]
    repos = result["repositories"]
    insights = result["insights"]
    
    print(f"\nAnalysis Date: {metadata['extracted_at']}")
    print(f"Total Repositories Analyzed: {len(repos)}")
    
    print("\n" + "-"*80)
    print("TOP 10 REPOSITORIES")
    print("-"*80)
    
    for i, repo in enumerate(repos, 1):
        print(f"\n{i}. {repo['full_name']}")
        print(f"   Stars: {repo['stars']:,}")
        print(f"   Language: {repo['language']}")
        print(f"   Description: {repo['description'][:100]}{'...' if len(repo['description'] or '') > 100 else ''}")
        print(f"   URL: {repo['url']}")
    
    print("\n" + "-"*80)
    print("BUSINESS INSIGHTS")
    print("-"*80)
    
    tech_dir = insights["technical_direction"]
    print(f"\n📊 Technical Direction:")
    print(f"   Dominant Language: {tech_dir['dominant_language']}")
    print(f"   Language Distribution:")
    for lang, data in tech_dir["language_distribution"].items():
        print(f"      {lang}: {data['count']} ({data['percentage']}%)")
    print(f"   Technology Trends: {', '.join(tech_dir['tech_trends']) if tech_dir['tech_trends'] else 'None identified'}")
    
    activity = insights["activity_analysis"]
    print(f"\n📈 Activity Analysis:")
    print(f"   Star Distribution:")
    for level, count in activity["star_distribution"].items():
        print(f"      {level.capitalize()}: {count}")
    print(f"   Average Stars: {activity['average_stars']:,}")
    print(f"   Popularity Score: {activity['popularity_score']}")
    
    risks = insights["risk_assessment"]
    print(f"\n⚠️ Risk Assessment:")
    if risks:
        for risk in risks:
            print(f"   {risk['repo']}:")
            for r in risk['risks']:
                print(f"      - {r}")
    else:
        print("   No significant risks identified")
    
    # Print JSON result for programmatic use
    print("\n" + "-"*80)
    print("JSON OUTPUT (for programmatic use)")
    print("-"*80)
    print(json.dumps(result, indent=2, default=str))

if __name__ == "__main__":
    main()