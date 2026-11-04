---
title: Publications
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-book-open" %}Publications

{% include section.html %}

## Selected Publications

{% include list.html data="citations" component="citation" style="rich" filter="highlight == true" %}

{% include section.html %}

## Publications from UC Berkeley

{% include list.html data="citations" component="citation" style="rich" filter="group == 'berkeley'" %}

{% include section.html %}

## Publications from the Leibniz-Forschungsinstitut für Molekulare Pharmakologie (FMP), Berlin

{% include list.html data="citations" component="citation" style="rich" filter="group != 'early' and group != 'berkeley'" %}

{% include section.html %}

## Master Thesis and Research Associate Publications

{% include list.html data="citations" component="citation" filter="group == 'early'" %}
