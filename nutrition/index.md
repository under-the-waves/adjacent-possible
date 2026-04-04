---
life_area_slug: nutrition
---
[← Back to Home](../)
# Food and Nutrition

## Why Food and Nutrition Matter

Food choices affect virtually every aspect of life, from physical health and longevity to cognitive function, environmental sustainability, and financial wellbeing. Poor diet is the leading risk factor for death globally, responsible for more deaths than tobacco, high blood pressure, or any other risk <span class="info-icon" onclick="showReasoning('research-gbd')">i</span>. Yet diet quality in most developed countries is remarkably low -- the average American scores just 59 out of 100 on the Healthy Eating Index, and only 10-12% of adults meet basic fruit and vegetable intake recommendations <span class="info-icon" onclick="showReasoning('research-diet-quality')">i</span>.

Beyond personal health, food decisions carry significant ethical implications. The global food system is responsible for roughly 26% of anthropogenic greenhouse gas emissions, with animal products accounting for the majority of that impact <span class="info-icon" onclick="showReasoning('research-environment')">i</span>. Food is also deeply intertwined with culture, pleasure, and social connection -- shared meals strengthen relationships and food traditions carry cultural identity across generations <span class="info-icon" onclick="showReasoning('research-social')">i</span>. Optimising nutrition should enhance, not diminish, these dimensions.

## Food and Nutrition Values

Your approach to nutrition depends on which aspects you value most. This guide balances three core values, with percentages indicating the relative weight given to each in our recommendations.

For personalised recommendations based on your unique priorities, visit [Nutrition Personalised]({{ site.baseurl }}/nutrition/personalised), where you can adjust these value weightings to see which interventions work best for your specific goals and preferences.

{% include life-area-values.html %}

## Benchmarks by Level

{% include life-area-benchmarks.html %}

## Personalisation

- [Nutrition Personalised]({{ site.baseurl }}/nutrition/personalised)

[← Back to Life Areas]({{ site.baseurl }}/life-areas/)

<script>
const researchData = {
    'research-gbd': {
        title: 'Diet as Leading Risk Factor',
        content: 'The Global Burden of Disease study found that dietary risks are the leading risk factor for deaths globally, associated with 11 million deaths per year -- more than tobacco smoking (8 million), high blood pressure (10.4 million), or any other risk factor. The main dietary risks are high sodium intake, low whole grain intake, and low fruit intake. <a href="https://doi.org/10.1016/S0140-6736(19)30041-8" target="_blank">GBD 2017 Diet Collaborators, The Lancet 2019</a>'
    },
    'research-diet-quality': {
        title: 'Population Diet Quality',
        content: 'The average Healthy Eating Index score for US adults is approximately 59 out of 100 (USDA CNPP data). Only 12.3% of adults meet fruit intake recommendations and 10% meet vegetable recommendations. In the UK, average fibre intake is 19g/day against a recommendation of 30g, with only 9% meeting the target. <a href="https://www.cdc.gov/mmwr/volumes/71/wr/mm7101a1.htm" target="_blank">CDC MMWR 2022</a>; <a href="https://www.gov.uk/government/statistics/ndns-results-from-years-9-to-11-2016-to-2017-and-2018-to-2019" target="_blank">UK NDNS</a>'
    },
    'research-environment': {
        title: 'Food System Environmental Impact',
        content: 'A comprehensive meta-analysis of 38,700 farms found that food production is responsible for approximately 26% of global greenhouse gas emissions, 70% of freshwater use, and 78% of freshwater eutrophication. Animal products provide just 18% of calories but account for 58% of food emissions. Moving from current diets to plant-based diets could reduce food-related emissions by up to 73%. <a href="https://doi.org/10.1126/science.aaq0216" target="_blank">Poore & Nemecek, Science 2018</a>'
    },
    'research-social': {
        title: 'Social Dimensions of Eating',
        content: 'Research consistently shows that sharing meals strengthens social bonds and improves wellbeing. People who eat socially more often feel happier and are more satisfied with their lives, more trusting of others, and more engaged with their local communities. These associations hold after controlling for personality, income, and other social activities. <a href="https://doi.org/10.1016/j.appet.2017.01.007" target="_blank">Dunbar, Appetite 2017</a>'
    },
    {% include benchmark-reasoning.html %}
};

</script>

{% include popup-boilerplate.html %}
