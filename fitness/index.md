---
life_area_slug: fitness
---
[← Back to Home](../)
# Fitness

## Why Fitness Matters

Fitness serves as a cornerstone of overall wellbeing, influencing virtually every aspect of daily life. Regular physical activity strengthens your cardiovascular system and builds muscle and bone density, while simultaneously improving memory, concentration, and creative thinking <span class="info-icon" onclick="showReasoning('research-cognitive')">i</span>. The neurochemical changes from exercise effectively combat depression and anxiety, creating cascading benefits in mood, relationships, and life satisfaction <span class="info-icon" onclick="showReasoning('research-mental-health')">i</span>.

Fitness also boosts confidence, whilst extending both lifespan and "healthspan" – the period of life spent in good health. Regular exercisers have a 30-40% lower risk of all-cause mortality <span class="info-icon" onclick="showReasoning('research-mortality')">i</span>. These combined benefits make fitness one of the highest-leverage investments you can make in your quality of life.

## Fitness Values

Your approach to fitness depends on which aspects you value most. This guide balances three core values, with percentages indicating the relative weight given to each in our recommendations.

For personalised recommendations based on your unique priorities, visit [Fitness Personalised]({{ site.baseurl }}/fitness/personalised), where you can adjust these value weightings to see which interventions work best for your specific goals and preferences.

{% include life-area-values.html %}

Looking for fitness interventions focused on weight loss or muscle gain? Visit [Body Image]({{ site.baseurl }}/body-image/), where the same fitness interventions are scored on appearance-specific values like fat loss and muscle gain.

## Benchmarks by Level

{% include life-area-benchmarks.html %}

## Personalisation

- [Fitness Personalised]({{ site.baseurl }}/fitness/personalised)

[← Back to Life Areas]({{ site.baseurl }}/life-areas/)

<script>
const researchData = {
    'research-cognitive': {
        title: 'Exercise and Cognitive Function',
        content: 'A systematic review and meta-analysis found that regular aerobic exercise significantly improves executive function, memory, and processing speed. Even a single bout of moderate exercise can enhance attention and working memory for several hours. <a href="https://bjsm.bmj.com/content/52/3/154" target="_blank">Northey et al., British Journal of Sports Medicine 2018</a>'
    },
    'research-mental-health': {
        title: 'Exercise and Mental Health',
        content: 'A landmark study of 1.2 million US adults found that those who exercised had 43% fewer days of poor mental health per month than non-exercisers. Exercise is now recommended as a first-line treatment for mild-moderate depression by NICE guidelines. <a href="https://jamanetwork.com/journals/jamapsychiatry/article-abstract/2720689" target="_blank">Chekroud et al., The Lancet Psychiatry 2018</a>'
    },
    'research-mortality': {
        title: 'Exercise and Longevity',
        content: 'A meta-analysis of over 800,000 participants found that regular physical activity reduces all-cause mortality risk by 30-40%. The benefits follow a dose-response curve, with the greatest gains from moving from sedentary to moderately active. Even 15 minutes of daily exercise extends lifespan by approximately 3 years. <a href="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(12)61031-9/fulltext" target="_blank">Wen et al., The Lancet 2011</a>'
    },
    {% include benchmark-reasoning.html %}
};

</script>

{% include popup-boilerplate.html %}
