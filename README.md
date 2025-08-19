# Computer Science

A comprehensive collection of algorithms, interview prep, cloud/GCP utilities, data projects, and hands-on examples. This repo serves as a personal knowledge base and a set of ready-to-run references across computer science topics.

## Overview

This repository contains organized submodules covering:
- **Algorithms & Data Structures** - Python implementations and practice problems
- **Interview Preparation** - CTCI, LeetCode, Codility solutions
- **Data Science Projects** - Visualization and mining projects with comprehensive documentation
- **Cloud & DevOps** - GCP, Terraform, Kubernetes, Cloud Run implementations
- **Databases** - PostgreSQL, NoSQL, and big data coursework
- **Web Development** - Django applications and utilities
- **Security & Networking** - VPN, infosec, and security tools
- **System Design** - Distributed systems and architecture patterns

## Repository Structure

### 🧮 **Algorithms & Data Structures**
- **`algorithms/`** - Comprehensive algorithm implementations
  - `leetcode/` - LeetCode problem solutions
  - `codility/` - Codility coding challenges
  - `ctci/` - Cracking the Coding Interview solutions
  - `DynamicProgramming/` - DP algorithm implementations
  - `Backtracking/` - Backtracking algorithm examples
  - `dsap/` - Data Structures and Algorithms practice
  - `interview/` - Interview-specific problems and tips
  - `mathProblems/` - Mathematical problem solutions
  - `pythonic_stuff/` - Python-specific implementations

### 📊 **Data Science Projects**
- **`data-visualization/`** - Data visualization course projects
  - `assignments/` - Course assignments with comprehensive documentation
  - `documentation/` - Course materials and guides
  - `final-project/` - Adult income analysis project
  - Interactive runner script for easy execution
- **`data-mining/`** - Machine learning projects for diabetes management
  - `datasets/` - CGM and insulin data files
  - `projects/` - Meal detection, time series analysis, clustering validation
  - `documentation/` - Project guides and methodology
  - Interactive runner script for easy execution

### ☁️ **Cloud & DevOps**
- **`gcp/`** - Google Cloud Platform implementations
  - `app-engine/` - App Engine applications
  - `cloudrun/` - Cloud Run services
  - `cloudfunctions/` - Cloud Functions
  - `kubernetes/` - GKE and Kubernetes configurations
  - `iam/` - Identity and Access Management
  - `networks/` - VPC, VPN, and networking
  - `storage/` - Cloud Storage implementations
  - `billing/` - Billing and cost management
  - `security/` - Security configurations
  - `profiling/` - Performance profiling tools
  - `ai-ml/` - AI/ML implementations
    - `vertex-ai-mlops/` - Comprehensive Vertex AI MLOps workflows and examples
- **`terraform/`** - Infrastructure as Code
  - Infrastructure templates and modules
  - State management and dependencies
- **`canary-bg/`** - Canary deployment implementations
  - Cloud Run deployment strategies
  - Traffic management and rollback procedures
- **`grafana_prometheus/`** - Monitoring and observability
  - Grafana dashboards and Prometheus configurations

### 🗄️ **Databases**
- **`databases/`** - Database coursework and implementations
  - `postgres/` - PostgreSQL assignments and projects
  - `bigData/` - Big data analysis projects
  - `unQLlite/` - NoSQL database implementations

### 🌐 **Web Development**
- **`Django/`** - Django web applications
  - SSN security project
  - Web application templates and utilities

### 🔒 **Security & Networking**
- **`infosec/`** - Information security projects
  - Security tools and implementations
- **`kali/`** - Kali Linux security tools
  - Penetration testing and security utilities
- **`open-vpn/`** - VPN implementations
  - Terraform configurations for VPN setup

### 🔧 **System Design & Architecture**
- **`python-grpc/`** - gRPC implementations
  - Microservices communication patterns
- **`gws/`** - Google Workspace APIs
  - Directory API, Reports API, Data Transfer API
- **`sre-interview-prep-guide/`** - Site Reliability Engineering
  - Interview preparation materials and guides

### 📚 **Learning Resources**
- **`google-interview-university/`** - Google Interview University
  - Comprehensive interview preparation guide
- **`machine-learning/`** - Machine learning resources
  - Supervised and unsupervised learning materials
- **`pythonicStuff/`** - Python best practices
  - Pythonic patterns and utilities
- **`ctci/`** - Cracking the Coding Interview
  - Chapter-wise solutions and implementations

### 🎯 **Specialized Projects**
- **`quality-of-life/`** - Quality of Life application (uninitialized)
  - Web application for quality of life metrics

## Quick Start

### Clone (with submodules)

```bash
# Recommended: clone with submodules
git clone --recurse-submodules git@github.com-personal:mkmad/computer-science.git
cd computer-science

# If already cloned without submodules
git submodule update --init --recursive
```

### Python environment

```bash
# Optional: use a specific Python version if defined
pyenv install -s $(cat .python-version 2>/dev/null || echo 3.11.0)
pyenv local $(cat .python-version 2>/dev/null || echo 3.11.0)

# Install dependencies for specific projects
cd data-visualization && pip install -r requirements.txt
cd ../data-mining && pip install -r requirements.txt
```

## Project Highlights

### Data Science Projects

#### data-visualization/
- **Purpose**: Course assignments and final project for data visualization
- **Structure**: Organized into assignments, documentation, and final project
- **Quick Start**:
  ```bash
  cd data-visualization
  pip install -r requirements.txt
  python run_examples.py
  ```

#### data-mining/
- **Purpose**: Machine learning projects for diabetes management
- **Structure**: Datasets, projects (meal detection, time series, clustering), documentation
- **Quick Start**:
  ```bash
  cd data-mining
  pip install -r requirements.txt
  python run_examples.py
  ```

### Cloud & DevOps

#### gcp/
- **Purpose**: Google Cloud Platform implementations and utilities
- **Key Areas**: App Engine, Cloud Run, Kubernetes, IAM, Networking, Security, AI/ML
- **Usage**: Each subdirectory contains specific GCP service implementations
- **Submodules**: 
  - `ai-ml/vertex-ai-mlops/` - Comprehensive Vertex AI MLOps workflows and examples

#### terraform/
- **Purpose**: Infrastructure as Code templates
- **Usage**: Deploy infrastructure using Terraform configurations

#### canary-bg/
- **Purpose**: Canary deployment strategies for Cloud Run
- **Usage**: Traffic management and gradual rollouts

#### gcp/ai-ml/vertex-ai-mlops/
- **Purpose**: Comprehensive Vertex AI MLOps workflows and examples
- **Content**: AutoML, BigQuery ML, scikit-learn, TensorFlow, PyTorch, XGBoost, R implementations
- **Usage**: End-to-end machine learning operations on Google Cloud Platform
- **Quick Start**:
  ```bash
  cd gcp/ai-ml/vertex-ai-mlops
  # Follow the setup instructions in the README
  ```



### Algorithms & Interview Prep

#### algorithms/
- **Purpose**: Comprehensive algorithm implementations and practice
- **Coverage**: LeetCode, Codility, CTCI, Dynamic Programming, Backtracking
- **Usage**: Reference implementations and practice problems

#### ctci/
- **Purpose**: Cracking the Coding Interview solutions
- **Structure**: Chapter-wise organized solutions
- **Usage**: Interview preparation and algorithm practice

## Submodules Management

This repository uses Git submodules extensively. Here are the key submodules:

### Core Learning Submodules
- `google-interview-university/` - Interview preparation guide
- `machine-learning/` - ML resources and materials
- `algorithms/` - Algorithm implementations
- `ctci/` - CTCI solutions
- `pythonicStuff/` - Python best practices

### Data Science Submodules
- `data-visualization/` - Data visualization projects
- `data-mining/` - Machine learning projects

### Cloud & DevOps Submodules
- `gcp/` - Google Cloud Platform implementations
  - `ai-ml/vertex-ai-mlops/` - Vertex AI MLOps workflows
- `terraform/` - Infrastructure as Code
- `canary-bg/` - Canary deployments
- `grafana_prometheus/` - Monitoring and observability

### Database & Web Submodules
- `databases/` - Database coursework
- `Django/` - Django web applications

### Security & Networking Submodules
- `infosec/` - Information security
- `kali/` - Security tools
- `open-vpn/` - VPN implementations

### System Design Submodules
- `python-grpc/` - gRPC implementations
- `gws/` - Google Workspace APIs
- `sre-interview-prep-guide/` - SRE materials

### Specialized Submodules
- `quality-of-life/` - Quality of life application (uninitialized)
- `distributed-systems/` - Distributed systems patterns

### Submodule Commands

- **Add a submodule**
```bash
git submodule add <remote_url> <destination_folder>
git commit -m "Add submodule"
```

- **Update/initialize submodules**
```bash
git submodule update --init --recursive
```

- **Update submodules to latest remote commits**
```bash
git submodule foreach git fetch --all
git submodule foreach git checkout main || true
git submodule foreach git pull --ff-only || true
```

- **Remove a submodule**
```bash
# 1) Edit .gitmodules and remove the entry
# 2) Stage the change
git add .gitmodules
# 3) Remove from git config
# 4) Untrack the submodule
git rm --cached path_to_submodule
# 5) Remove the submodule's git dir
rm -rf .git/modules/path_to_submodule
# 6) Commit and delete working tree files
git commit -m "Remove submodule"
rm -rf path_to_submodule
```

- **Manage nested submodules** (e.g., submodules within submodules)
```bash
# Navigate to the parent submodule
cd gcp
# Update the nested submodule
git submodule update --remote ai-ml/vertex-ai-mlops
# Commit and push changes
git add ai-ml/vertex-ai-mlops
git commit -m "Update nested submodule"
git push origin main
```

## Repository Statistics

- **Total Submodules**: 20+ organized repositories
- **Categories**: 8 major areas of computer science
- **Languages**: Python, JavaScript, TypeScript, Terraform, SQL, R
- **Cloud Platforms**: Google Cloud Platform, AWS (via Terraform)
- **Data Science**: Visualization, Mining, Machine Learning
- **Architecture**: Microservices, Distributed Systems, MLOps

## Contributing

- Keep edits scoped and documented in the relevant folder `README.md`
- Match existing code style and avoid noisy reformatting
- Prefer small, focused commits with clear messages
- Update submodule references when making changes to submodules

## License

Educational and personal reference material. Respect licenses of third-party materials and datasets included within subfolders.