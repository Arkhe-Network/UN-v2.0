validate-schemas:
	@echo "Validating schemas..."

gen-stubs:
	@echo "Generating stubs..."
	buf generate proto

test-e2e:
	@echo "Running E2E tests..."
	PYTHONPATH=tests/e2e pytest tests/e2e/test_pix_zk_flow.py -v -m fast -p asyncio

dev-up:
	@echo "Starting dev environment..."

deploy-aws:
	@echo "Deploying to AWS..."

terraform-apply:
	@echo "Applying terraform..."
