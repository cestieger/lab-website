---
---

<div class="lab-hero">
  <img src="{{ 'images/logo.svg' | relative_url }}" alt="Stieger Lab logo">
  <div class="lab-hero-text">
    <h1>Stieger Lab</h1>
    <p class="lab-hero-sub">Chemical Biology and Induced Proximity</p>
  </div>
</div>

{% include section.html %}

{% capture text %}

The Stieger Lab works at the interface of synthetic chemistry, chemical biology and drug discovery. Many diseases are driven by transcription factors, proteins that switch genes on or off but lack the binding pockets that conventional drugs rely on.

We combine new covalent chemistries, high-throughput discovery of peptide and peptidomimetic ligands, and genome-wide profiling of chromatin and gene expression to develop chemical inducers of proximity. These molecules recruit chromatin-regulating enzymes to disease-relevant transcription factors and reprogram the genes they control. Our long-term goal is new therapeutic strategies against cancer and a deeper understanding of how chromatin regulation shapes gene expression.

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
  image="images/research-figure-v3.png"
  image2="images/research-structure.jpg"
  link="research"
  title="Research"
  text=text
%}

{% capture text %}

The Stieger Lab opens at TUM in January 2027, and we are building our team. We are looking for curious people at all levels: PhD students, Master's and Bachelor's thesis students, and a student assistant. Whether your background is in organic synthesis, chemical biology, biochemistry, cell biology or pharmaceutical sciences, there is a project for you.

Interested? Just drop Christian an email and let's chat about science!

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
  title="Your Lab Coat Is Waiting"
  text=text
%}

{% comment %}
Team section hidden for now. To show it again, delete the comment and endcomment lines around it.

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
  link="team"
  title="Team"
  flip=true
  text=text
%}
{% endcomment %}
