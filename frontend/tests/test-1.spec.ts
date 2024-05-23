import { test, expect } from '@playwright/test';

test.only('test', async ({ page }) => {
  test.slow();
  await page.goto('https://adalogix.es/');
  await page.goto('https://adalogix.es/login');
  await page.getByLabel('Username').click();
  await page.getByLabel('Username').fill('alehd642');
  await page.getByLabel('Password').click();
  await page.getByLabel('Password').click();
  await page.getByLabel('Password').fill('Z9KlyHVB6Wtb');
  await page.getByRole('button', { name: 'Log in' }).click();
  await expect(page.getByRole('toolbar').getByText('Orders')).toBeVisible();
  await expect(page.getByLabel('Expand "alejandro hd"')).toBeVisible();
  await page.goto('https://adalogix.es/inventories');
  await expect(page.getByText('Records per page:')).toBeVisible();
  await page.goto('https://adalogix.es/employees');
  await expect(page.getByText('Records per page:')).toBeVisible();
  await page.goto('https://adalogix.es/router');
  await page.locator('button').filter({ hasText: 'chevron_left' }).click();
  await expect(page.locator('div').filter({ hasText: /^Courier$/ }).first()).toBeVisible();
  await page.goto('https://adalogix.es/chat');
  await expect(page.getByRole('heading', { name: 'Adalogix' })).toBeVisible();
  await page.getByLabel('Expand "alejandro hd"').click();
  await page.getByRole('button', { name: 'Logout' }).click();
  await page.getByRole('button', { name: 'Yes' }).click();
  await page.getByRole('button', { name: 'OK' }).click();
  await expect(page.getByRole('button', { name: 'Log in' })).toBeVisible();
});
