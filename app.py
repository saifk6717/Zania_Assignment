from pdf_extractor import extract_text_from_pdf, split_text_into_chunks
from question_answering import get_answer_from_text
from slack_client import post_results_to_slack

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    text_chunks = split_text_into_chunks(text)
    
    while True:
        question = input("Enter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break

        answers = []
        for chunk in text_chunks:
            answer = get_answer_from_text(question, chunk)
            if answer != "Data Not Available":
                answers.append(answer)
        
        combined_answer = ' '.join(answers)
        if combined_answer:
            final_answer = combined_answer[:500] + '...' if len(combined_answer) > 500 else combined_answer
        else:
            final_answer = "Data Not Available"
        
        print(f"Answer: {final_answer}")
        
        post_to_slack = input("Do you want to post this answer to Slack? (yes/no): ").strip().lower()
        if post_to_slack == 'yes':
            post_results_to_slack({question: final_answer})

if __name__ == "__main__":
    pdf_path = r"C:\Assignment\New Zania\handbook.pdf"  # Use raw string for Windows paths
    main(pdf_path)
