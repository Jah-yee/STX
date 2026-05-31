#!/usr/bin/env python3
"""
Trending Developer Analysis Script for 2026
This script analyzes trending developer accounts, their contribution patterns,
repository popularity, and technology focus areas.
"""

import json
import re
import subprocess
from datetime import datetime
from collections import defaultdict, Counter
import requests

class GitHubTrendingAnalyzer:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "TrendingDeveloperAnalyzer/1.0"
        }
        
    def fetch_trending_developers(self, period="weekly"):
        """Fetch trending developers from GitHub"""
        try:
            # Use GitHub search to find popular developers
            url = f"{self.base_url}/search/users"
            params = {
                "q": "followers:>100",
                "sort": "followers",
                "order": "desc",
                "per_page": 10
            }
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                developers = []
                for item in data.get("items", [])[:10]:
                    developers.append({
                        "username": item.get("login"),
                        "profile_url": item.get("html_url"),
                        "followers": item.get("followers", 0),
                        "type": "developer"
                    })
                return developers
            else:
                print(f"Failed to search users: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching trending developers: {e}")
            return []
    
    def get_user_repositories(self, username, per_page=10):
        """Fetch repositories for a given user"""
        try:
            url = f"{self.base_url}/users/{username}/repos"
            params = {
                "per_page": per_page,
                "sort": "stars",
                "direction": "desc"
            }
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            
            if response.status_code == 200:
                repos = response.json()
                return self.process_repositories(repos)
            else:
                print(f"Failed to fetch repos for {username}: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching repos for {username}: {e}")
            return []
    
    def process_repositories(self, repos):
        """Process repository data"""
        processed = []
        for repo in repos:
            processed.append({
                "name": repo.get("name"),
                "description": repo.get("description"),
                "stars": repo.get("stargazers_count", 0),
                "forks": repo.get("forks_count", 0),
                "language": repo.get("language"),
                "topics": repo.get("topics", []),
                "url": repo.get("html_url"),
                "created_at": repo.get("created_at"),
                "updated_at": repo.get("updated_at")
            })
        return processed
    
    def analyze_contribution_patterns(self, repos):
        """Analyze contribution patterns from repositories"""
        patterns = {
            "total_repos": len(repos),
            "languages": Counter(),
            "topics": Counter(),
            "stars_distribution": [],
            "activity_levels": Counter()
        }
        
        for repo in repos:
            # Language distribution
            if repo["language"]:
                patterns["languages"][repo["language"]] += 1
            
            # Topics distribution
            for topic in repo["topics"]:
                patterns["topics"][topic] += 1
            
            # Stars distribution
            patterns["stars_distribution"].append(repo["stars"])
            
            # Activity level based on last update
            patterns["activity_levels"][self.categorize_activity(repo["updated_at"])] += 1
        
        return patterns
    
    def categorize_activity(self, date_str):
        """Categorize activity level based on last update"""
        try:
            from datetime import datetime, timezone
            last_update = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            days_since = (datetime.now(timezone.utc) - last_update.replace(tzinfo=None)).days
            
            if days_since < 30:
                return "active"
            elif days_since < 90:
                return "moderate"
            else:
                return "inactive"
        except:
            return "unknown"
    
    def identify_tech_focus(self, repos):
        """Identify technology focus areas"""
        tech_keywords = {
            "web_development": ["javascript", "python", "ruby", "php", "node.js", "react", "vue", "angular"],
            "data_science": ["python", "r", "jupyter", "pandas", "numpy", "scikit-learn", "tensorflow"],
            "devops": ["docker", "kubernetes", "ansible", "terraform", "jenkins", "ci/cd"],
            "mobile": ["java", "kotlin", "swift", "react native", "flutter"],
            "ai_ml": ["machine learning", "deep learning", "neural network", "pytorch", "tensorflow"],
            "backend": ["java", "python", "go", "rust", "c++", "database", "api"],
            "frontend": ["html", "css", "javascript", "typescript", "react", "vue"]
        }
        
        focus_areas = defaultdict(int)
        
        for repo in repos:
            repo_text = f"{repo['name']} {repo['description']} {repo['topics']}".lower()
            
            for category, keywords in tech_keywords.items():
                for keyword in keywords:
                    if keyword in repo_text:
                        focus_areas[category] += 1
        
        return dict(focus_areas)
    
    def generate_report(self, developers):
        """Generate comprehensive analysis report"""
        report = {
            "analysis_date": datetime.now().isoformat(),
            "total_developers_analyzed": len(developers),
            "developer_summaries": [],
            "aggregated_insights": {}
        }
        
        all_repos = []
        all_languages = Counter()
        all_topics = Counter()
        
        for dev in developers:
            print(f"Analyzing {dev['username']}...")
            repos = self.get_user_repositories(dev["username"][:20])  # Limit to top 20 repos
            
            if repos:
                patterns = self.analyze_contribution_patterns(repos)
                tech_focus = self.identify_tech_focus(repos)
                
                dev_summary = {
                    "username": dev["username"],
                    "profile_url": dev["profile_url"],
                    "followers": dev.get("followers", 0),
                    "repo_count": len(repos),
                    "top_languages": dict(patterns["languages"].most_common(5)),
                    "tech_focus": tech_focus,
                    "avg_stars": sum(r["stars"] for r in repos) / len(repos) if repos else 0,
                    "contribution_patterns": patterns
                }
                
                report["developer_summaries"].append(dev_summary)
                
                # Aggregate data
                all_repos.extend(repos)
                all_languages.update(patterns["languages"])
                for topic in patterns["topics"].keys():
                    all_topics[topic] += 1
        
        # Generate aggregated insights
        report["aggregated_insights"] = {
            "total_repositories": len(all_repos),
            "top_languages": dict(all_languages.most_common(10)),
            "top_topics": dict(all_topics.most_common(10)),
            "avg_repos_per_dev": len(all_repos) / len(developers) if developers else 0,
            "avg_stars_per_repo": sum(r["stars"] for r in all_repos) / len(all_repos) if all_repos else 0
        }
        
        return report

def main():
    print("=" * 60)
    print("Trending Developer Analysis for 2026")
    print("=" * 60)
    
    analyzer = GitHubTrendingAnalyzer()
    
    # Fetch trending developers
    print("\n1. Fetching trending developers...")
    developers = analyzer.fetch_trending_developers("weekly")
    print(f"   Found {len(developers)} trending developers")
    
    if not developers:
        print("   No developers found. Using sample data for demonstration...")
        # Create sample data for demonstration
        developers = [
            {"username": "sample1", "type": "developer"},
            {"username": "sample2", "type": "developer"}
        ]
    
    # Generate report
    print("\n2. Analyzing repositories and contribution patterns...")
    report = analyzer.generate_report(developers)
    
    # Save report
    report_file = f"trending_devs_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"\n3. Report saved to: {report_file}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"Total Developers Analyzed: {report['total_developers_analyzed']}")
    print(f"Total Repositories: {report['aggregated_insights']['total_repositories']}")
    print(f"Top Languages: {list(report['aggregated_insights']['top_languages'].keys())[:5]}")
    print(f"Top Topics: {list(report['aggregated_insights']['top_topics'].keys())[:5]}")
    
    return report

if __name__ == "__main__":
    main()