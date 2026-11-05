---
---

# Stieger Lab - Chemical Biology and Induced Proximity

[LAB MISSION: 1-3 sentences describing what the lab does]

{% include section.html %}

{% capture text %}

[RESEARCH SUMMARY: a short paragraph on the lab's research themes]

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
  image="images/photo.jpg"
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
  image="images/photo.jpg"
  link="join"
  title="Join us"
  text=text
%}
