# src/query_modeler.py

from typing import List, Dict

class QueryLanguageModeler:
    """
    Compiles query threads cohesively for AI model benchmarking.
    """

    def __init__(self, context: str = ""):
        """
        context: Optional global context for all queries
        """
        self.context = context

    def compile_queries(self, keywords: List[str]) -> List[Dict]:
        """
        Converts a list of keywords into structured query threads.
        Returns a list of dicts with 'keyword' and 'structured_prompt'.
        """
        query_threads = []
        for kw in keywords:
            structured_prompt = self._create_structured_prompt(kw)
            query_threads.append({
                "keyword": kw,
                "structured_prompt": structured_prompt
            })
        return query_threads

    def _create_structured_prompt(self, keyword: str) -> str:
        """
        Generates a cohesive prompt for AI models.
        """
        prompt = f"{self.context}\nProvide a detailed, informative response about '{keyword}'."
        return prompt

    def merge_responses(self, responses: Dict[str, str]) -> str:
        """
        Optionally merge multiple model responses into a cohesive summary.
        `responses` is a dict {model_name: response_text}
        """
        summary = "### Cohesive Summary of AI Model Responses\n"
        for model, resp in responses.items():
            summary += f"\n**{model}**:\n{resp}\n"
        return summary
