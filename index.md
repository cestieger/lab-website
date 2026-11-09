---
---

<div class="lab-hero">
  <img src="{{ 'images/logo.svg' | relative_url }}" alt="Stieger Lab logo">
  <div class="lab-hero-text">
    <h1 id="stieger-lab">Stieger Lab</h1>
    <p class="lab-hero-sub">Chemical Biology and Induced Proximity</p>
  </div>
</div>

[LAB MISSION: 1-3 sentences describing what the lab does]

{% include section.html %}

{% capture text %}

The Stieger Lab works at the interface of synthetic chemistry, chemical biology and drug discovery. Many diseases are driven by transcription factors, specialized proteins that control which genes are switched on or off. Because most transcription factors lack the binding pockets that conventional drugs rely on, they have remained notoriously difficult to target.

To address this challenge, we combine new covalent chemistries, high-throughput discovery of peptide and peptidomimetic ligands, and genome-wide profiling of chromatin states and gene expression. These tools enable us to develop bifunctional chemical inducers of proximity that recruit chromatin-regulating enzymes to disease-relevant transcription factors, reprogramming the transcriptional programs they control.

Our long-term goal is to develop new therapeutic strategies that exploit the transcriptional dependencies of cancer cells, and to better understand how chromatin regulation shapes cancer-associated gene expression.

{%
  include button.html
  link="research"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Research"
  text=text
%}

{% capture text %}

Meet the people behind the lab.

{%
  include button.html
  link="team"
  text="Meet the team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/christian-stieger.jpg"
  link="team"
  title="Team"
  flip=true
  text=text
%}

{% capture text %}

We are recruiting a PhD student, Master's and Bachelor's thesis students, and a student assistant.

{%
  include button.html
  link="join"
  text="See open positions"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/tum-building.jpg"
  link="join"
  title="Join us"
  text=text
%}
