# E2-Standard-4 running in GCE

Simple conversation with 2 turns

| User              | Agent      |
| ----------------- | ---------- |
| Hi there          | <response> |
| Tell me about GKE | <response> |

````json
INFO:     98.51.189.208:53360 - "POST /sessions HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192/events",
  "status_code": 200,
  "duration_seconds": 0.112
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192",
  "status_code": 200,
  "duration_seconds": 0.115
}
INFO:     98.51.189.208:54097 - "POST /chat HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192/events",
  "status_code": 200,
  "duration_seconds": 0.074
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192",
  "status_code": 200,
  "duration_seconds": 0.127
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.105
}
INFO:google_adk.google.adk.models.google_llm:Sending out request, model: gemini-2.5-flas...d: GoogleLLMVariant.VERTEX_AI, stream: True
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/global/publishers/google/models/gemini-2.5-flash-lite:streamGenerateContent?alt=sse",
  "status_code": 200,
  "duration_seconds": 0.493
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.101
}
INFO:sessions_server:runner.run_async enumeration loop completed in 5.0659 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192",
  "status_code": 200,
  "duration_seconds": 0.076
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192/events",
  "status_code": 200,
  "duration_seconds": 0.092
}
INFO:sessions_server:Updated session get completed in 1.1938 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192",
  "status_code": 200,
  "duration_seconds": 0.087
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192/events",
  "status_code": 200,
  "duration_seconds": 0.099
}
INFO:     98.51.189.208:54168 - "POST /chat HTTP/1.1" 200 OK
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192",
  "status_code": 200,
  "duration_seconds": 0.086
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192/events",
  "status_code": 200,
  "duration_seconds": 0.103
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.086
}
INFO:google_adk.google.adk.models.google_llm:Sending out request, model: gemini-2.5-flas...d: GoogleLLMVariant.VERTEX_AI, stream: True
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/global/publishers/google/models/gemini-2.5-flash-lite:streamGenerateContent?alt=sse",
  "status_code": 200,
  "duration_seconds": 0.482
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "POST",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192:appendEvent",
  "status_code": 200,
  "duration_seconds": 0.092
}
INFO:sessions_server:runner.run_async enumeration loop completed in 5.8626 seconds
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192",
  "status_code": 200,
  "duration_seconds": 0.073
}
INFO:http_timing:HTTP Request:
{
  "type": "http_request",
  "method": "GET",
  "url": "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/jwd-gcp-demos/locations/us-central1/reasoningEngines/3246018909450534912/sessions/5274066732493832192/events",
  "status_code": 200,
  "duration_seconds": 0.097
}
INFO:sessions_server:Updated session get completed in 1.0490 seconds
````