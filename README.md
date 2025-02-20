# 🌾 Agricultural Plan Optimization

## 📌 Project Overview

This project focuses on **optimizing agricultural production** in Algeria using **Artificial Intelligence (AI)** techniques. The goal is to maximize **agricultural yield**, minimize **costs**, and enhance **self-sufficiency** in key agricultural products across different wilayas.

**🧑‍💻 Team Members:**
- **MEFTAH Zineb (Leader)**
- **BENAMGHAR Amina**
- **DJOUBANI Sarah**
- **BENMANSOUR Aya**

---

## 📊 Data Description

The project is based on **agricultural production data** from various wilayas, detailing:
- **Available land** for agriculture.
- **Production efficiency** per hectare.
- **Cost structures** for key agricultural products.

---

## 🎯 Problem Definition

The project aims to **strategically optimize agricultural production** by balancing:
1. **📈 Highest Production**: Maximizing agricultural yield per hectare.
2. **💰 Lowest Cost**: Ensuring cost-effective production while maintaining fair pricing for farmers.
3. **🌍 Self-Sufficiency**: Reducing reliance on imports by encouraging sustainable farming practices.

---

## 🏗️ General Graph Search Approach

**🔎 Problem Formulation:**
- **Initial State**: Empty strategic plan with available land and unassigned production.
- **Transition Model**: Each action modifies land use and production levels for a specific wilaya.
- **Goal Test**: Achieve self-sufficiency and optimal land utilization within price constraints.
- **Path Cost**: Total production cost considering land use, labor, and resource expenditure.

### 🚀 Search Strategies Implemented:
- **Depth-First Search (DFS) 🏗️** – Explores deeply before backtracking.
- **Uniform Cost Search (UCS) 💰** – Finds the lowest-cost production strategy.
- **A* Algorithm 🌟** – Uses heuristics to optimize land usage and self-sufficiency.
- **Hill Climbing 🏔️** – Locally optimizes production allocation but can get stuck in local optima.

---

## 🔢 Constraint Satisfaction Problem (CSP)

The **CSP model** ensures:
- **Self-Sufficiency Constraint**: The agricultural production ratio must be ≥1.
- **Maximization Constraint**: Production is maximized within a given price threshold.
- **Land Constraints**: Allocations respect available land in each wilaya.

### ✨ Key Methods:
- **Land Set Generation**: Computes possible land allocations per wilaya.
- **Domain Filtering**: Eliminates infeasible land values dynamically.
- **Backtracking Algorithm**: Solves the optimization problem by iterating through possible values.

---

## 📈 Comparative Analysis of Search Algorithms

| Algorithm  | Execution Time (ms) | Nodes Explored | Efficiency |
|------------|--------------------|---------------|------------|
| **DFS**  | 72.37  | 124  | 🚨 Inefficient (Explores too many nodes) |
| **UCS**  | 55.26  | 107  | ✅ Finds least-cost path |
| **A*** | 49.99  | 100  | 🏆 Best performance |
| **Hill Climbing** | 66.48  | 121  | ⚠️ Can get stuck in local optima |

**Conclusion:**
- **A*** is the most efficient search method.
- **UCS** is effective when heuristics are unavailable.
- **DFS** performs poorly in large search spaces.

---

## 🖥️ Visualization & Results

- The **final strategic agricultural plan** is computed using CSP and search algorithms.
- Graphical **comparisons of efficiency** between different search strategies.
- Interactive **map visualizations** for optimized agricultural planning.

---

## 🤝 Team Contribution

All members actively participated in **data analysis, search algorithms, and constraint satisfaction problem formulation**. Weekly meetings were held to discuss progress and refine solutions.

---

## 📚 References

- **Official Climate & Agricultural Reports**  
  - [Weather & Climate Data](https://weatherandclimate.com/algeria)  
  - [Algerian Population Data](https://www.populationdata.net/pays/algerie/divisions)  
  - [Ministry of Agriculture Reports](https://madr.gov.dz/wp-content/uploads/2022/04/SERIE-B-2019.pdf)  
- **Farmer Consultation**  
  - Expert: *Bachir Kaouachi*

---

## 🏁 Conclusion

This project demonstrates how **AI-driven optimization** can revolutionize **agriculture planning** in Algeria. By integrating **graph search techniques** and **constraint satisfaction modeling**, it provides a **scalable**, **cost-efficient**, and **sustainable** agricultural strategy.

🚀 *Future work includes real-time data integration and machine learning for predictive analysis.*

---

🌱 **Optimizing Agriculture, Ensuring Sustainability!** 🌍  
