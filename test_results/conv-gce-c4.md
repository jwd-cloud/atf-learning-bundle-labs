# C4-Standard-4 running in GCE

Simple conversation with 2 turns

| User              | Agent      |
| ----------------- | ---------- |
| Hi there          | <response> |
| Tell me about GKE | <response> |

````json
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992",
  "status_code": 200,
  "duration_seconds": 0.097
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992/events",
  "status_code": 200,
  "duration_seconds": 0.103
}
INFO:     98.51.189.208:63400 - "POST /chat HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992",
  "status_code": 200,
  "duration_seconds": 0.084
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992/events",
  "status_code": 200,
  "duration_seconds": 0.097
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.103
}
INFO:google_adk.google.adk.models.google_llm:Sending out request, model: gemini-2.5-flas...d: GoogleLLMVariant.VERTEX_AI, stream: True
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/global/publishers/google/models/gemini-2.5-flash-lite:streamGenerateContent?alt=sse",
  "status_code": 200,
  "duration_seconds": 0.81
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.092
}
INFO:sessions_server_mp:runner.run_async enumeration loop completed in 3.3338 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992/events",
  "status_code": 200,
  "duration_seconds": 0.074
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992",
  "status_code": 200,
  "duration_seconds": 0.092
}
INFO:sessions_server_mp:Updated session get completed in 0.5705 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992/events",
  "status_code": 200,
  "duration_seconds": 0.081
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992",
  "status_code": 200,
  "duration_seconds": 0.082
}
INFO:     98.51.189.208:63459 - "POST /chat HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992",
  "status_code": 200,
  "duration_seconds": 0.068
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992/events",
  "status_code": 200,
  "duration_seconds": 0.07
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.087
}
INFO:google_adk.google.adk.models.google_llm:Sending out request, model: gemini-2.5-flas...d: GoogleLLMVariant.VERTEX_AI, stream: True
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/global/publishers/google/models/gemini-2.5-flash-lite:streamGenerateContent?alt=sse",
  "status_code": 200,
  "duration_seconds": 0.613
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.075
}
INFO:sessions_server_mp:runner.run_async enumeration loop completed in 3.0410 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992/events",
  "status_code": 200,
  "duration_seconds": 0.085
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/221590900537556992",
  "status_code": 200,
  "duration_seconds": 0.117
}
INFO:sessions_server_mp:Updated session get completed in 0.5862 seconds
````